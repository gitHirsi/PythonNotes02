"""
@Author : Hirsi
@ Time :  2020/7/5
"""
"""
return的作用
    可以结束生成器的运行
send的作用
    生成器.send(传递给生成器的值)
    例：fib.send(1)
       xxx = yield data    # xxx = 1
"""

def fibnacci(num):
    a = 1
    b = 1

    index = 0
    while index < num:
        data = a
        a, b = b, a + b
        index += 1

        x = yield data
        if x == data:
            return '我是return，我终止了生成器'


fib = fibnacci(10)
print(next(fib))
try:
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(fib.send(3))

except Exception as ex:
    print(ex)
