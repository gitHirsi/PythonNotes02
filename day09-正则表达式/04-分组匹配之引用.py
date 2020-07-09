"""
@Author : Hirsi
@ Time :  2020/7/7
"""
"""
\1 ： 表示引用第一个分组
   \\1 ： \\表示转义字符，转义后代表一个\ 
"""
import re

#                                     \1          \ 有特殊用法
#                                     \\  转移成  \
# result = re.match('<([a-zA-Z0-9]+)>.*</\\1>', '<html>test</html>')

result = re.match('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\\2></\\1>', '<html><h1>test</h1></html>')

if result:
    print('匹配成功:', result.group())
    print('提取字符串:', result.group(1),result.group(2))
else:
    print('匹配失败!')