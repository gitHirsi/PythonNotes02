"""
@Author : Hirsi
@ Time :  2020/7/2
"""

"""
结束进程 ：终端输入-->   kill -9 进程编号
"""
import multiprocessing
import time
import os

def work():
    for i in range(10):
        # print('正在运行work...',multiprocessing.current_process())

        # 获取进程的编号
        # print('正在运行work...',multiprocessing.current_process().pid)

        # 使用os模块来获取进程id
        # print('正在运行work...', os.getpid())

        #获得进程的父id
        print('正在运行work... 第',i,'次', os.getpid(),'--->父id',os.getppid())
        time.sleep(2)

if __name__ == '__main__':
    # 获取主进程的名称
    print(multiprocessing.current_process())


    # 1)获取进程的编号 Process id --->pid
    print('主进程编号:',multiprocessing.current_process().pid)

    # 2)使用os模块来获取主进程id
    # print(os.getpid())


    # target 制定子进程要执行的分支函数  name 制定子进程的名称
    p1 = multiprocessing.Process(target=work,name='进程1')
    p1.start()

    print('xxx')