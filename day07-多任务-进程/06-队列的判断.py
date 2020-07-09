"""
@Author : Hirsi
@ Time :  2020/7/3
"""

"""
添加完数据不阻塞一下，判断是否为空，队列里有消息，也为空  time.sleep(0.00001)
"""
import multiprocessing
import time

queue = multiprocessing.Queue(3)
queue.put(1)
queue.put(2)
queue.put(3)

# 添加完数据不阻塞一下，判断是否为空，有消息，也为空
time.sleep(0.00001)

# 取出消息
# queue.get()

# 1.判断是否已满
print('队列是否已满-->',queue.full())

# 2.获取队列中消息的个数
print('队列中消息的个数-->',queue.qsize())


# queue.get()
# 3.判断是否为空
isEmpty = queue.empty()
print('队列是否为空-->',isEmpty)