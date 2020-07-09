"""
@Author : Hirsi
@ Time :  2020/6/29
"""

import socket as so
from day05.application import app


class WebServer(object):
    def __init__(self):
        tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
        # 设置地址重用
        tcp_server_so.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, True)
        tcp_server_so.bind(('', 12138))
        tcp_server_so.listen(128)

        # 定义实例属性，保存套接字对象
        self.tcp_server_so = tcp_server_so

    def start(self):
        """ 启动web服务器"""
        while True:
            new_client_so, ip_port = self.tcp_server_so.accept()
            print(f'客户端{ip_port}已连接~~')
            self.request_headler(new_client_so, ip_port)

    # 接受客户端浏览器发送的请求协议
    def request_headler(self, new_client_so, ip_port):
        request_data = new_client_so.recv(1024)
        if not request_data:
            print(f'客户端{ip_port}已断开~~')
            new_client_so.close()
            return

        # 调用app模块
        response_data = app.application('static', request_data)


        new_client_so.send(response_data)

        new_client_so.close()


def main():
    ws = WebServer()
    ws.start()


if __name__ == '__main__':
    main()
