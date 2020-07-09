"""
@Author : Hirsi
@ Time :  2020/7/3
"""

"""
思路(线程池)
    1.定义变量，保存源文件夹，目标文件夹所在的路径
    2.在目标路径创建新的文件夹
    3.获取源文件夹中所有的文件(列表)
    4.便利列表，得到所有的文件名
    5.定义函数，进行文件拷贝
    文件拷贝函数 参数(源文件夹路径，目标文件夹路径，文件名)
        1.拼接源文件和目标文件的具体路径
        2.打开源文件，创建目标文件
        3.读取源文件的内容，写入到目标文件中(while)
"""
import os
import multiprocessing
import time

# 5.定义函数，进行文件拷贝
def copy_work(source_dir,dest_dir,file_name):
    print(multiprocessing.current_process().name)
    # 1.拼接源文件和目标文件的具体路径,打开源文件，创建目标文件
    source_path=source_dir+'/'+file_name
    dest_path=dest_dir+'/'+file_name
    # 3.读取源文件的内容，写入到目标文件中(while)
    with open(source_path,'rb') as source_file:
        with open(dest_path,'wb') as dest_file:
            while True:
                read_data = source_file.read(1024)
                if read_data:
                    dest_file.write(read_data)
                    time.sleep(0.5)
                else:
                    break


if __name__ == '__main__':
    # 1.定义变量，保存源文件夹，目标文件夹所在的路径
    source_dir='./test'
    dest_dir='/home/hirsi/桌面/test'
    # 2.在目标路径创建新的文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print('文件已存在!')
    # 3.获取源文件夹中所有的文件(列表)
    file_list = os.listdir(source_dir)

    # ***创建进程池
    pool = multiprocessing.Pool(3)

    # 4.遍历列表，得到所有的文件名
    for file_name in file_list:
        # 单进程
        # copy_work(source_dir,dest_dir,file_name)
        pool.apply_async(copy_work,(source_dir,dest_dir,file_name))

    # 不再接受新的任务
    pool.close()
    # 让主进程等待进程池结束后再退出
    pool.join()
    print('复制完成!')