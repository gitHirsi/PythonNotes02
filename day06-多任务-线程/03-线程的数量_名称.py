"""
@Author : Hirsi
@ Time :  2020/6/30
"""

import time
import threading


def sing():
    for i in range(5):
        print('正在唱歌...', threading.current_thread())
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞...', threading.current_thread())
        time.sleep(1)


if __name__ == '__main__':
    # 线程的名称
    print(threading.current_thread())

    thread_list = threading.enumerate()
    print('1线程的数量:', len(thread_list))

    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)
    thread_sing.start()
    thread_dance.start()

    # while True:
    #     thread_num = len(threading.enumerate())
    #     print('2线程的数量:', thread_num)
    #
    #     # 如果只剩下主线程就停止循环
    #     if thread_num <= 1:
    #         break
    #
    #     time.sleep(0.5)
