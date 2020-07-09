"""
@Author : Hirsi
@ Time :  2020/7/7
"""

"""
贪婪   : 满足正则的情况下，尽可能的多取内容 (默认为贪婪模式)
非贪婪 : 满足正则的情况下，尽可能的少取内容
    在+ * ？{} 后面添加? 可以变成非贪婪
"""

import re

# result1 = re.match('gasman\d+', 'gasman12138')
# result2 = re.match('gasman\d+?', 'gasman12138')
#
# if result1 and result2:
#     print('匹配贪婪结果:',result1.group())
#     print('匹配非贪婪结果:', result2.group())

# else:
#     print('匹配失败!')

str1 = """
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" 
src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
"""

# result3 = re.search('src=\"(.*?)\"', str1)
result3 = re.search('src="(.*?)"', str1)

if result3:
    print('匹配结果:',result3.group())
    print('地址:',result3.group(1))
else:
    print('匹配失败！')