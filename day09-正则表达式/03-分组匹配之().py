"""
@Author : Hirsi
@ Time :  2020/7/7
"""
"""
() 作用 : 
    1) 分组，组内整体匹配
    2) 提取字符串 result.group(1)   result.group(2)
"""
import re

olEmail = 'mmmmmmmmmmm@outlook.com'
qqEmail = '123456789@qq.com'
_163Email = 'hhhhhhhhhh@163.com'
result1 = re.match('\w{6,20}@(163|126|qq|outlook)\.com', olEmail)

if result1:
    print('匹配成功:', result1.group())
    print('提取字符串:', result1.group(1))
else:
    print('匹配失败!')

"""提取区号和电话号码"""

result2 = re.match('(\d{3,4})-(\d{7,8})', '0722-4719788')
if result2:
    print("区号:",result2.group(1))
    print("电话号码:",result2.group(2))
else:
    print('匹配失败!')