"""
@Author : Hirsi
@ Time :  2020/6/30
"""
"""
子线程创建的步骤:
    1.导入模块 threading
    2.使用threading.Thread() 创建对象
    3.制定子线程执行的分支
    4.启动子线程的线程对象
"""

import threading
import time


def saySorry():
    print('对不起，我错了!',threading.current_thread().name)
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        # 2.使用threading.Thread()创建对象
        # 3.制定子线程执行的分支
        # threading.Thread(target=函数名)
        thread_obj = threading.Thread(target=saySorry)
        # 线程只有调用了start（） 子线程才会执行
        thread_obj.start()

    print('xxxxxxxx')
