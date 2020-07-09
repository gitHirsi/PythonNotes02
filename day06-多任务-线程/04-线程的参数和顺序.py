"""
@Author : Hirsi
@ Time :  2020/6/30
"""

import time
import threading


def sing(a, b, c):
    print('参数:', a, b, c)

    for i in range(5):
        print('正在唱歌...')
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞......')
        time.sleep(1)


if __name__ == '__main__':
    # 传递参数的三种方法
    # 1.使用元组传递参数 threading.Thread(target=sing,args=(12,34,56))
    # thread_sing = threading.Thread(target=sing,args=(12,34,56))

    # 2.使用字典传递 threading.Thread(target=sing, kwargs={'a': 10, 'b': 100, 'c': 1000})
    # thread_sing = threading.Thread(target=sing, kwargs={'a': 10, 'b': 100, 'c': 1000})

    # 3.使用元组和字典传递 threading.Thread(target=sing,args=(10,),kwargs={'b':100,'c':1000})
    thread_sing=threading.Thread(target=sing,args=(10,),kwargs={'b':100,'c':1000})

    thread_dance = threading.Thread(target=dance)
    thread_sing.start()
    thread_dance.start()
