import yagmail
# 使用yagmail的类创建发件人对象(发件人邮箱,邮箱授权码,邮箱的服务器)
ya_obj = yagmail.SMTP(user='hirsiboom@163.com',password='AKWHQZPSRGLEXHDM',host='smtp.163.com')
# 要发送的内容
content='helli ,LiuYun,you are dog!'
# 使用yagmail创建的发送人对象发送邮件(制定收件人邮箱,邮件的主题,要发送的内容)
ya_obj.send('10255871@qq.com','TestOne',content)