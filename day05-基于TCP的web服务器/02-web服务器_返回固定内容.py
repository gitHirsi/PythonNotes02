"""
@Author : Hirsi
@ Time :  2020/6/24
"""

"""
简单的web服务器（TCP）_返回固定内容
1.导入模块
2.创建套接字
3.设置地址重用
4.绑定端口
5.设置监听，让套接字由主动变为被动接受
6.接受客户端连接  定义函数 request_headler（）
7.接受客户端浏览器发送的请求协议
8.判断协议是否为空
9.拼接相应的报文
10.发送相应的报文
11.关闭操作
"""
# 1
import socket as so


# 6 接受客户端连接  定义函数
def request_headler(new_client_so, ip_port):
    # 7
    recv_data = new_client_so.recv(1024)
    # 8
    if not recv_data:
        print(f'客户端{ip_port}已下线!')
        new_client_so.close()
        return

    # 9 拼接相应的报文
    # 9.1 响应行
    response_line = 'HTTP/1.1 200 OK\r\n'
    # 9.2 响应头
    response_header = 'Server:Python20WS/2.0\r\n'
    # 9.3 响应空行
    response_blank = '\r\n'
    # 9.4 响应主体
    response_body = "<h1><font color='Green'>Hello Python</font></h1>"

    response_data = response_line + response_header + response_blank + response_body

    # 10 发送相应的报文
    new_client_so.send(response_data.encode())

    new_client_so.close()


def main():
    # 2
    tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
    # 3
    tcp_server_so.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, True)
    # 4
    tcp_server_so.bind(('', 12138))
    # 5
    tcp_server_so.listen(128)
    while True:
        new_client_so, ip_port = tcp_server_so.accept()
        print(f'客户端{ip_port}已上线')
        request_headler(new_client_so, ip_port)

    # 11
    # tcp_server_so.close()


if __name__ == '__main__':
    main()
