"""
@Author : Hirsi
@ Time :  2020/7/1
"""
"""
多线程之间可以共享全局变量
"""
import threading
import time

g_num = 0


def work1():

    global g_num
    for i in range(10):
        g_num += 1
    print('work1：',g_num)

def work2():
    print('work2:',g_num)

if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    t1.start()
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print('main:', g_num)
