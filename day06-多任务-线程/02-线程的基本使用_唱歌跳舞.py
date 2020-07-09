"""
@Author : Hirsi
@ Time :  2020/6/30
"""
import time
import threading

def sing():
    for i in range(5):
        print('正在唱歌...')
        time.sleep(1)

def dance():
    for i in range(5):
        print('正在跳舞...')
        time.sleep(1)

if __name__ == '__main__':
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)
    thread_sing.start()
    thread_dance.start()
