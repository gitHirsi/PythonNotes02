"""
@Author : Hirsi
@ Time :  2020/6/23
"""

"""
1.导入模块
2.创建套接字
3.建立连接
4.拼接请求协议
5.发送请求协议
6.接受服务器相应的内容
7.保存内容
8.关闭连接
"""

# 1.导入模块
import socket as so

# 2.创建套接字
tcp_client_so = so.socket(so.AF_INET, so.SOCK_STREAM)

# 3.建立连接
tcp_client_so.connect(('www.baidu.com', 80))

# 4.拼接请求协议
# 4.1请求行
# request_line = 'GET / HTTP/1.1\r\n'
# # 4.2请求头
# request_header = 'Host:www.baidu.com\r\n'
# # 4.3请求空行
# request_blank = '\r\n'
# request_data = request_line + request_header + request_blank
request_data = 'GET / HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n'

# 5.发送请求协议
tcp_client_so.send(request_data.encode())

# 6.接受服务器相应的内容
html_data = ''
while True:
    recv_data = tcp_client_so.recv(1024).decode()
    if recv_data:
        html_data += recv_data
    else:
        break

# 7 保存内容（切片截取html的内容）
html_loc = html_data.find('\r\n\r\n')
html_text = html_data[html_loc + 4:]
# print(html_text)
with open('baidu.html', 'w') as file:
    file.write(html_text)

# 8.关闭连接

tcp_client_so.close()
