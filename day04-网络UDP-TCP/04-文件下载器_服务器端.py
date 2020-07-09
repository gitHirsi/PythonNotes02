"""
@Author : Hirsi
@ Time :  2020/6/22
"""

"""
1.导入模板
2.创建套接字
3.1 绑定端口   3.2设置套接字地址可以重用 
4.设置监听，设置套接字由主动变被动
5.接受客户端的连接
6.接受客户端发送的文件名
7.根据文件名读取文件内容
8.把读取的文件内容发送给客户端（循环发送）
9.关闭和当前客户端的连接
10.关闭服务器
"""

import socket as so

# 创建服务端的套接字，并绑定端口
tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
tcp_server_so.bind(('', 8080))

# ******设置套接字地址可以重用********
# tcp_server_so.setsockopt(当前套接字 ， 属性名 ， 属性值)
# so.SO_REUSEADDR ： 地址是否可以重用  Ttue 可以重用  False 不可以
tcp_server_so.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, True)

# 4
tcp_server_so.listen(128)
# 5
while True:
    new_client_so, client_ip_port = tcp_server_so.accept()
    print(f'{client_ip_port}客户端已连接....')

    # 6
    file_name = new_client_so.recv(1024).decode()

    try:
        # 7 读取文件内容
        with open(file_name, 'rb') as file:
            # file = open(file_name, 'rb')
            while True:
                file_data = file.read(1024)
                if file_data:
                    new_client_so.send(file_data)
                else:
                    break

    except:
        print(f'文件{file_name}不存在！')
    else:

        print('下载成功！')

    # 9 关闭和当前客户端的连接
    new_client_so.close()

# 10 关闭服务器
tcp_server_so.close()
