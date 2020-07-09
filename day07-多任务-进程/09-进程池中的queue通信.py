"""
@Author : Hirsi
@ Time :  2020/7/3
"""
"""
1.创建进程池中的队列 >>> queue = multiprocessing.Manager().Queue(n)  n:表示队列的长度
2.apply_async()返回值ApplyResult对象，该对象有个wait()方法,类似join()
    >>> pool.apply_async(write_que,(queue,)).wait()
"""
import multiprocessing
import time

# 写入数据到队列的函数
def write_que(queue):
    for i in range(10):
        if queue.full():
            print('队列已满!')
            break
        queue.put(i)
        print(f'{i}写入')
        time.sleep(0.3)

# 读取队列数据的函数
def read_que(queue):
    print('-------------')
    while not queue.empty():
        print('取出:',queue.get())
        time.sleep(0.3)
    else:
        print('队列已为空！')

if __name__ == '__main__':
    #1.创建进程池
    pool = multiprocessing.Pool(2)
    #2.***创建进程池中的队列queue
    queue = multiprocessing.Manager().Queue(5)
    #3.使用进程池执行任务
    # 3.1)同步方式
    # pool.apply(write_que,(queue,))
    # pool.apply(read_que,(queue,))

    #3.2)异步方式⬇
    # apply_async()返回值ApplyResult对象，该对象有个wait()方法,类似join()
    pool.apply_async(write_que,(queue,)).wait()
    pool.apply_async(read_que,(queue,))

    # 不再接受新的任务
    pool.close()
    # 主进程等待进程池执行结束后再退出
    pool.join()

