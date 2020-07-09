"""
@Author : Hirsi
@ Time :  2020/7/2
"""
"""
进程之间不能实现全局变量的共享   
    底层原理:子进程都是把资源复制了一份到内部进行操作
"""

import multiprocessing
import time

g_num = 10

def work1():
    # 全局变量要修改，在函数里要声明
    global g_num
    for i in range(10):
        g_num += 1
    print('work1:',g_num)

def work2():
    print('work2:',g_num)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work1)
    p2 = multiprocessing.Process(target=work2)
    p1.start()
    time.sleep(1)
    p2.start()

    time.sleep(1)

    print('main:',g_num)
