"""
@Author : Hirsi
@ Time :  2020/7/3
"""

"""
思路:利用队列在两个进程间进行传递，进而实现数据共享
1.准备两个进程
2.准备一个队列,一个进程向队列写入数据，然后另外一个进程读取队列李的数据
    注:优先让写数据进程执行结束后，在执行读取数据的进程  p1.join()
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
        print(f'{i}写入成功')
        time.sleep(0.3)

    time.sleep(0.00001)


# 读取队列数据的函数
def read_que(queue):
    print('-------------')
    while not queue.empty():
        print('取出:', queue.get())
        time.sleep(0.3)
    else:
        print('队列已为空！')


if __name__ == '__main__':
    # 创建一个空的队列
    queue = multiprocessing.Queue(5)

    # 创建两个进程
    p1 = multiprocessing.Process(target=write_que, args=(queue,))
    p2 = multiprocessing.Process(target=read_que, args=(queue,))

    p1.start()

    # ***优先让写数据进程执行结束后，在执行读取数据的进程
    p1.join()

    p2.start()
