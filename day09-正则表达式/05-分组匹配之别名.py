"""
@Author : Hirsi
@ Time :  2020/7/7
"""
"""
起别名:?P<name1>
用别名:(?P=name2)
"""
import re

# result = re.match('<([a-zA-Z0-9]+)>.*</\\1>', '<html>test</html>')
result = re.match('<(?P<name1>[a-zA-Z0-9]+)><(?P<name2>[a-zA-Z0-9]+)>.*</(?P=name2)></(?P=name1)>', '<html><h1>test</h1></html>')

if result:
    print('匹配成功:', result.group())
    print('提取字符串:', result.group(1),result.group(2))
else:
    print('匹配失败!')