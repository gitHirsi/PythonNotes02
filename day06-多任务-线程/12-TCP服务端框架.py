"""
@Author : Hirsi
@ Time :  2020/7/1
"""
import socket as so
import threading

"""
1.导入模块
2.创建套接子
3.设置地址可重用
4.绑定端口
5.设置监听,套接字由主动设置为被动
6.接受客户端连接
7.接受客户端发送的信息
8.解码数据并且进行输出
9.关闭和当前客户端的连接
支持多线程 思想 : 每来一个新的客户端，就创建一个新的线程用来接受信息
"""

def recv_msg(new_client_so,ip_port):
    while True:
        # 7.接受客户端发送的信息
        recv_data = new_client_so.recv(1024)
        if recv_data:
            # 8.解码数据并且进行输出
            recv_text = recv_data.decode('GBK')
            print(f'来自{ip_port}的:{recv_text}')
        else:
            break

    # 9.关闭和当前客户端的连接
    new_client_so.close()


# 2.创建套接子
tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
# 3.设置地址可重用
tcp_server_so.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, True)
# 4.绑定端口
tcp_server_so.bind(('', 12138))
# 5.设置监听,套接字由主动设置为被动
tcp_server_so.listen(128)

while True:
    # 6.接受客户端连接
    new_client_so, ip_port = tcp_server_so.accept()
    print(f'客户端{ip_port}上线>>>')
    
    # 创建线程
    t1 = threading.Thread(target=recv_msg,args=(new_client_so,ip_port))
    t1.setDaemon(True)  #守护线程
    t1.start()   #开启线程

    print(len(threading.enumerate()))

# tcp_server_so.close()