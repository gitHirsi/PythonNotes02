"""
@Author : Hirsi
@ Time :  2020/6/22
"""

"""
1.导入模块
2.创建套接字
3.建立连接
4.接受用户输入的文件名
5.发送文件名到服务器
6.创建文件，并准备保存
7.接受服务器发送的数据，保存曹本地（循环写入保存）
8.关闭套接字
"""

import socket as so

tcp_client_so = so.socket(so.AF_INET, so.SOCK_STREAM)
tcp_client_so.bind(('',12138))
# 3
tcp_client_so.connect(('192.168.1.5',8080))
# 4
file_name = input('请输入要下载的文件名:')
# 5
tcp_client_so.send(file_name.encode())

# 6.创建文件，并准备保存
with open('/home/hirsi/桌面/'+file_name,'wb') as file:
    # 7.接受服务器发送的数据，保存曹本地（循环写入保存）
    while True:
        recv_data = tcp_client_so.recv(1024)
        if recv_data:
            file.write(recv_data)
        else:
            break

# 8
tcp_client_so.close()

"""
bug:文件不存在服务器，也会在本地建立一个同名空内容文件
"""
