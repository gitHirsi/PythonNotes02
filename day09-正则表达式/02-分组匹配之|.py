"""
@Author : Hirsi
@ Time :  2020/7/7
"""
""" 
 |  : 表示或者关系，对个正则表达式满足任意一个都可以 
"""
import re

result = re.match('^[0-9]?[0-9]$|^100$', '100') #成功
result = re.match('^[0-9]?[0-9]$|^100$', '99')  #成功

if result:
    print('匹配成功!')
    print('匹配结果:', result.group())

else:
    print('匹配失败!')
