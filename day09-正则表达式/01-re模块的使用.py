"""
@Author : Hirsi
@ Time :  2020/7/7
"""
"""
1.导入模块
2.通过match()，验证正则   是必须从字符串开头位置匹配，如果失败返回None
    re.match(正则表达式,要验证/检索的字符串)
        match() 如果匹配成功，返回match object 对象
        match() 如果匹配失败，返回None
3.判断 验证/检索是否成功 
4.如果成功，获取匹配的结果 result.group()
    start()  返回匹配开始的位置
    end()    返回匹配结束的位置
    span()   返回⼀个元组包含匹配 (开始,结束) 的位置
"""
import re

result = re.match('hirsi', 'hirsiGasman12138')
# result = re.match('\w{6,20}@163\.com$', 'hirsiboom@163.com')
if result:
    print('匹配成功!')
    print('匹配结果:', result.group())

else:
    print('匹配失败!')
