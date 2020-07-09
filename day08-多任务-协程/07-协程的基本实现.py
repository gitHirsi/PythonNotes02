"""
@Author : Hirsi
@ Time :  2020/7/5
"""
"""
协程:
    1.在不开辟新线程的基础上，实现多个任务
    2.协程是一个特殊的生成器

"""

import time

# 创建work1生成器
def work1():
    while True:
        print('work1...')
        yield
        time.sleep(0.5)


# 创建work2生成器
def work2():
    while True:
        print('work2......')
        yield
        time.sleep(0.5)

# 获得生成器，通过next运行生成器
if __name__ == '__main__':
    w1=work1()
    w2=work2()

    while True:
        next(w1)
        next(w2)