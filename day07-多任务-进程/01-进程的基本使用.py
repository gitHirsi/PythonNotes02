"""
@Author : Hirsi
@ Time :  2020/7/2
"""

"""
1.导入模块
2.通过模块提供的Process类创建进程对象
3.启动进程
"""
import multiprocessing
import time

def work():
    for i in range(5):
        print('正在运行work...',i)
        time.sleep(0.5)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work)
    p1.start()

    print('xxx')
