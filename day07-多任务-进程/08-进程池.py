"""
@Author : Hirsi
@ Time :  2020/7/3
"""

"""
进程池:是进程的容器，可以自动帮我们创建制定数量的进程，并管理进程及工作
1.创建进程池  pool = multiprocessing.Pool(n)  n:表示最大允许n个进程
2.用进程池同步方式拷贝文件(同一时间只有一个进程在工作)  pool.apply(函数名,(参数1,参数2,.....))
3.用进程池异步方式拷贝文件(同一时间多个进程同时工作)  pool.apply_async(函数名,(参数1,参数2,.....))
    注:使用异步方式(apply_async)要注意两点
        1)pool.close() 表示不再接受新的任务
        2)主进程不再等待进程池执行结束后再退出，需要进程池pool.join()，表示让主进程等进程池结束后再退出
          
"""
import time
import multiprocessing

def copy_work():
    print('正在拷贝文件...',multiprocessing.current_process())
    time.sleep(0.5)

if __name__ == '__main__':
    # 创建进程池
    pool = multiprocessing.Pool(3)

    for i in range(10):
        # ***用进程池同步方式拷贝文件
        # pool.apply(copy_work)

        # ***用进程池异步方式拷贝文件
        pool.apply_async(copy_work)

    # # pool.close() 表示不再接受新的任务
    pool.close()

    # # 让主进程等进程池结束后再退出
    pool.join()