"""
@Author : Hirsi
@ Time :  2020/7/7
"""

"""
1.search  : 在字符串内匹配,返回值和match()一样 ---> re.search('\d+', '登录次数:235'),
2.findall : 在字符串中搜索全部，返回值是列表
3.sub     : 字符串替换(按照正则，在字符串内查找出来并且替换),返回值是替换后的字符串
            re.sub(正则, 新的内容, 要替换的字符串)
4.split   : 按照正则表达式拆分字符串,返回值是列表
            re.split(正则, 代拆分的字符串)
"""
import re

str1 = """<div>
<p>岗位职责： </p>
<p>完成推荐算法、 数据统计、 接⼝、 后台等服务器端相关⼯作</p>
<p><br></p>
<p>必备要求： </p>
<p>良好的⾃我驱动⼒和职业素养， ⼯作积极主动、 结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求： </p>
<p>1、 ⼀年以上 Python 开发经验， 掌握⾯向对象分析和设计， 了解设计模式</p>
<p>2、 掌握HTTP协议， 熟悉MVC、 MVVM等概念以及相关WEB开发框架</p>
<p>3、 掌握关系数据库开发设计， 掌握 SQL， 熟练使⽤ MySQL/PostgreSQL 中的⼀种<br></p>
<p>4、 掌握NoSQL、 MQ， 熟练使⽤对应技术解决⽅案</p>
<p>5、 熟悉 Javascript/CSS/HTML5， JQuery、 React、 Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项： </p>
<p>⼤数据， 数理统计， 机器学习， sklearn， ⾼性能， ⼤并发。 </p>
</div>"""

# 1
# result = re.search('hirsi', 'aahirsiGas12138')
# result = re.search('\d+', '登录次数:235')

# 2
result = re.findall('\d+', '登录次数:235,转发次数:666,评论次数:1036')

# 3
# result = re.sub('\d+', '12138', '登录次数:235,转发次数:666,评论次数:1036')
# <[^>]+> : 非 > 的一个元素，+就是有多个这个元素
# result = re.sub('<[^>]+>| |&nbsp;|\n','',str1)

# 4
# result = re.split(':| ', 'info:hirsiboom@163.com hirsi 23')

if result:
    print('匹配成功!')
    print('匹配结果:', result)

else:
    print('匹配失败!')
