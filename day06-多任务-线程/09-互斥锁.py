"""
@Author : Hirsi
@ Time :  2020/7/1
"""

"""
1.创建一把互斥锁   lock1 = threading.Lock()
2.在使用资源前要锁定资源    lock1.acquire()
3.使用完资源之后，释放资源   lock1.release()
"""

import threading
import time

g_num = 0


def work1():
    global g_num
    for i in range(1000000):
        # 锁定资源
        lock1.acquire()
        g_num += 1
        # 释放资源
        lock1.release()
    print('work1：', g_num)


def work2():
    global g_num
    for i in range(1000000):
        # 锁定资源
        lock1.acquire()
        g_num += 1
        # 释放资源
        lock1.release()
    print('work2:', g_num)


if __name__ == '__main__':
    # 1.创建一把互斥锁
    lock1 = threading.Lock()

    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    t1.start()
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print('main:', g_num)
