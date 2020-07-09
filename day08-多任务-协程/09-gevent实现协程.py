"""
@Author : Hirsi
@ Time :  2020/7/6
"""

"""
gevent的好处:能够自动识别程序中的耗时操作,在耗时的时候自动切换到其他任务
1.导入模块
2.指派任务

默认情况下 time.sleep(0.5) 不能被gevent识别为耗时操作
    解决: 1)把time.sleep(0.5) 换成 gevent.sleep(0.5)
          2)给gevent打补丁(如下👇👇⬇),让它识别time.sleep(0.5)

打🤪补丁:在不修改程序源代码的情况下，为程序增加新的功能
    步骤: 1)导入 monkey 模块 (from gevent import monkey）
          2)破解 monkey.patch_all()
          
猴⼦补丁主要有以下⼏个⽤处：
1. 在运⾏时替换⽅法、 属性等
2. 在不修改第三⽅代码的情况下增加原来不⽀持的功能
3. 在运⾏时为内存中的对象增加patch⽽不是在磁盘的源代码中增加
"""
# 一般方开头
from gevent import monkey
monkey.patch_all()

import time
import gevent


# 创建work1生成器
def work1():
    while True:
        print('work1...', gevent.getcurrent())
        time.sleep(0.5)
        # gevent.sleep(0.5)


# 创建work2生成器
def work2():
    while True:
        print('work2.........', gevent.getcurrent())
        time.sleep(0.5)
        # gevent.sleep(0.5)


# 获得生成器，通过next运行生成器
if __name__ == '__main__':
    # 指派任务
    # gevent.spawn(函数名, 参数1, 参数2, ...)
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    # 让主线程等待协程执行完毕再退出
    g1.join()
    g2.join()
