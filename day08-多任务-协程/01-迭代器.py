"""
@Author : Hirsi
@ Time :  2020/7/4
"""

"""
1.一个可迭代对象可以提供一个迭代器
2.iter(可迭代的对象):得到对象的迭代器
3.next(迭代器):得到下一个元素(调用迭代器里的__next__()方法)
迭代器特点：
    1）记录遍历的位置
    2) 配合next函数提供下一个元素的值
for循环的本质:
    1) 通过iter，获取要遍历对象的迭代器
    2）next(迭代器)获取下一个元素
    3) 帮我们捕获了异常StopIteration
自定义迭代器，满足两点:
    1)必须含有__iter__()
    2)且含有__next__()
"""

list1 = [1, 3, 5, 7, 9]

# 获取迭代器
iterator = iter(list1)

# 根据迭代器，获取下一个元素
next_value = next(iterator)
print(next_value)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# 超出对象的元素，停止迭代，报错
try:
    print(next(iterator))
except Exception as ex:
    print('对象元素取完，停止迭代')
