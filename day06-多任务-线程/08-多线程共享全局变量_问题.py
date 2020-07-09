"""
@Author : Hirsi
@ Time :  2020/7/1
"""
"""
当多个线程同时访问同一个资源，会出现资源竞争问题
    线程对象.join() : 可以让某个线程先执行
        缺点 : 把多线程变成了单线程,会影响整体性能
"""

import threading
import time

g_num = 0

def work1():

    global g_num
    for i in range(1000000):
        g_num += 1
    print('work1：',g_num)

def work2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('work2:',g_num)

if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    t1.start()
    # 优先让t1线程先执行，t1执行完毕后，t2才能执行
    t1.join()
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print('main:', g_num)
