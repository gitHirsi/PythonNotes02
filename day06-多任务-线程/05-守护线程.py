"""
@Author : Hirsi
@ Time :  2020/6/30
"""
"""
线程守护 : 子线程守护主线程 setDaemon(True)
"""
import time
import threading

def work1():
    for i in range(10):
        print('正在执行work1...',i)
        time.sleep(0.5)

if __name__ == '__main__':
    thread_work1 = threading.Thread(target=work1)

    # 线程守护
    thread_work1.setDaemon(True)
    thread_work1.start()

    time.sleep(2)
    print('Game Over!')
    exit()
    