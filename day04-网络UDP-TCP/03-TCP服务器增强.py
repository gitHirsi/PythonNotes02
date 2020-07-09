
"""
一个客户端连接一次，可以发送多条信息数据
"""

import socket as so

tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
tcp_server_so.bind(('', 12138))

tcp_server_so.listen(128)

new_client_so, client_ip_port = tcp_server_so.accept()
print(f'新客户端连接了>>>{client_ip_port}')

while True:
    recv_cont = new_client_so.recv(1024)
    # 当接收到的数据为空时，服务器端也要断开
    # len(recv_cont) != 0 >>>> recv_cont 非空即为真，否则为假
    if recv_cont:
        print(f"来自{client_ip_port}的:{recv_cont.decode('GBK')}")
    else:
        print(f'客户端{client_ip_port}已断开～')
        break

new_client_so.close()


tcp_server_so.close()