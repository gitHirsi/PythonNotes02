"""
@Author : Hirsi
@ Time :  2020/7/3
"""
"""
1.导入模块
2.创建队列  multiprocessing.Queue(n)  n:表示队列的长度
3.放值到里面  queue.put_nowait() : 队列满了，也不等待放入，直接报错
4.从队列取值  queue.get_nowait() : 当队列已空时，不会等待放入新的值，直接报错
"""
import multiprocessing

# 2.创建队列
queue = multiprocessing.Queue(5)
# 3.放值到里面
queue.put(2)
queue.put('boom')
queue.put([1, 2, 3])
queue.put((4, 5, 6))
queue.put({'name': 'Hirsi', 'age': 20})

# 放的值超出队列长度,队列就进入了阻塞状态，默认等待队列县取出值再放入值
# queue.put(6)

# ***队列满了，也不等待放入，直接报错
# queue.put_nowait(6)

# 4.取值  当队列为空的时候，再次get()取值，程序就会进入阻塞状态，等待放入新的值，再取出
for i in range(5):
    print(queue.get())

# ***当队列已空时，不会等待放入新的值，直接报错
# queue.get_nowait()
