"""
@Author : Hirsi
@ Time :  2020/7/4
"""
"""
1.可遍历对象就是可迭代对象
2.列表，元组，字典，字符串都是可迭代对象
3.自定义mycalss类对象是不可以迭代的
4.mycalss对象所属的类 MyClass 如果包含了__iter__()方法，此时myclass就是可迭代对象
5.故可迭代对象的本质，就是对象所属的类中包含了__iter__()方法
6.检测一个对象是否可以迭代，用isinstance() 函数检测
"""
from collections.abc import Iterable


ret = isinstance([1, 2, 3], Iterable)
print(ret)
print('--'*10)

ret2 = isinstance('hirsiboom', Iterable)
print(ret2)
print('--'*10)

class MyClass(object):

    # 增加一个魔术方法，该方法就是一个迭代器
    def __iter__(self):
        pass


my_class = MyClass()

ret1=isinstance(my_class,Iterable)
print(ret1)
print('--'*10)