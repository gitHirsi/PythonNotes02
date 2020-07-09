"""
@Author : Hirsi
@ Time :  2020/7/5
"""
"""
自定义迭代器得到斐波那契数列
    1）a保存第一列数据  b保存第二列数据
    2）a=b    b=a+b
    3) 取a的值，获得斐波那契数列
"""
import time

class Fibnacci(object):
    def __init__(self, num):
        self.num = num

        # 记录下标位置的实例属性
        self.current_index = 0
        # 定义变量保存斐波那契数列的第一列和第二列
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.num:
            # 定义变量，保存复制之前a的值(即数列的元素)
            data = self.a
            # a=b,b=a+b
            self.a, self.b = self.b, self.a + self.b
            # 下标位置+1
            self.current_index += 1
            # 返回a的值
            return data

        else:  # 超出下标值，主动抛出异常
            raise StopIteration

if __name__ == '__main__':
    f = Fibnacci(10)

    for i in f:
        print(i)
        # time.sleep(0.3)
