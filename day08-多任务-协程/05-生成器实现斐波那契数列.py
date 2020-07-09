"""
@Author : Hirsi
@ Time :  2020/7/5
"""

"""
yield 有两个作用
    1) 充当return的作用
    2) 保存程序的运行状态，并且暂停程序执行，下次从暂停的位置直接执行
"""


def fibnacci(num):
    a = 1
    b = 1
    # 定义变量当前生成的位置
    index = 0
    while index < num:
        data = a
        a, b = b, a + b
        index += 1
        yield data


if __name__ == '__main__':
    f = fibnacci(5)

    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))

    # x = 0
    # for i in f:
    #     x += 1
    #     print(f'{x}) {i}')
