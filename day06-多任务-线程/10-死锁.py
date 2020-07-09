"""
@Author : Hirsi
@ Time :  2020/7/1
"""

import threading

# 创建锁
lock = threading.Lock()


# 定义获取列表值得函数，参数为索引值
def get_value(index):
    # 定义列表
    data_list = [1, 3, 5, 7, 9]
    # 上锁
    lock.acquire()
    # 输出内容
    if index >= len(data_list):
        print("下标 %d 越界" % index)
        """ ***要在return 之前解锁,否则剩下的线程,等待线程5释放,才能锁定资源,故程序卡死***"""
        # return
        lock.release()
        return

    print(data_list[index])
    # 解锁
    lock.release()


if __name__ == '__main__':
    # 循环创建⼦线程访问列表
    for i in range(10):
        t1 = threading.Thread(target=get_value, args=(i,))
        t1.start()
