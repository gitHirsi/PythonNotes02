"""
@Author : Hirsi
@ Time :  2020/7/2
"""
"""
1.设置子进程守护主进程 --> 子进程名.daemon=True
2.终止子进程的执行 --> 子进程名.terminate
"""

import multiprocessing
import time


def work():
    for i in range(10):
        print('正在运行work...', i)
        time.sleep(0.5)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work)
    # 设置子进程守护主进程
    p1.daemon = True
    p1.start()

    time.sleep(2)
    print('主进程退出..')
    # 终止子进程的执行
    p1.terminate()
    exit()
