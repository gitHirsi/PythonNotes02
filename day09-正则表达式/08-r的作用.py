"""
@Author : Hirsi
@ Time :  2020/7/7
"""
"""
r的作用 : 让正则中的 \ 没有特殊含义(转义),仅代表原生的 \ 
"""
import re

result = re.match(r'<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\2></\1>', '<html><h1>test</h1></html>')

if result:
    print('匹配成功:', result.group())
    print('提取字符串:', result.group(1),result.group(2))
else:
    print('匹配失败!')