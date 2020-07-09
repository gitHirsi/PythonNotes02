"""
@Author : Hirsi
@ Time :  2020/7/5
"""
"""
greenlrt实现协程
    greenlet(函数名称)
    greenlet是一个第三方的模块，能实现自行调度的微线程
"""

import greenlet as gl
import time

# 创建work1生成器
def work1():
    while True:
        print('work1...')
        time.sleep(0.5)
        #切换到work2
        g2.switch()


# 创建work2生成器
def work2():
    while True:
        print('work2......')
        time.sleep(0.5)
        # 切换到work1任务
        g1.switch()

if __name__ == '__main__':
    # 创建greenlet的对象
    g1 = gl.greenlet(work1)
    g2 = gl.greenlet(work2)

    # 执行work1任务
    g2.switch()
