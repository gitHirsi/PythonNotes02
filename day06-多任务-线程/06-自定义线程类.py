"""
@Author : Hirsi
@ Time :  2020/7/1
"""
"""
1.让自定义类继承 threading.Thread 类
2.重写父类的run方法
3.通过创建子类对象，让子类对象调用start（）启动子线程 

自定义线程类的init方法问题
    子类先通过super调用父类的初始化方法，子类在初始化
"""
import threading
import time


# 自定义线程类
class MyThread(threading.Thread):
    def __init__(self, a):
        # 先要去调用父类的init方法
        super().__init__()
        self.a = a

    # 重写父类的run方法
    def run(self):
        for i in range(5):
            # self.name  是从父类继承的一个属性
            print('在执行子线程run方法', i, self.name,self.a)
            time.sleep(0.5)


if __name__ == '__main__':
    my_thread = MyThread(100)
    my_thread.start()

    print('xxxxx')
