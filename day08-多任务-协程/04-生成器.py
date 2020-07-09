"""
@Author : Hirsi
@ Time :  2020/7/5
"""
"""
生成器是一个特殊的迭代器(按照一定的规律生成数列)
    next(生成器) 也可获得下一个值
    
生成器的创建方式(两种)
    1) 列表推导式，把[]换成()
    2) 函数中使用了 yield
yield 有两个作用
    1) 充当return的作用
    2) 保存程序的运行状态，并且暂停程序执行，下次从暂停的位置直接执行
"""
list1 = [i * 2 for i in range(1, 10)]
print('列表list1:', list1)
print('-' * 40)
# 1)
list2 = (i * 2 for i in range(1, 10))

print(list2)
print(next(list2))
print(next(list2))

print('-' * 40)


# 2)
def test1():
    return 100


a = test1()
print('a:', a)


# 使用yield创建一个生成器
def test2():
    yield 100


# b是一个生成器对象
b = test2()
print(b)

print(next(b))
