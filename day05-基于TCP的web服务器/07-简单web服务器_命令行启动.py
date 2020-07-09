"""
@Author : Hirsi
@ Time :  2020/6/29
"""

import socket as so
import sys
from application import app


class WebServer(object):
    def __init__(self , port):
        tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
        # 设置地址重用
        tcp_server_so.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, True)
        tcp_server_so.bind(('', port))
        tcp_server_so.listen(128)

        # 定义实例属性，保存套接字对象
        self.tcp_server_so = tcp_server_so

    def start(self):
        """ 启动web服务器"""
        print('服务器启动成功...')
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
        print(request_data.decode())


        new_client_so.send(response_data)

        new_client_so.close()

"""
1.导入sys模块
2.获取系统传递到程序的参数
3.判断参数格式是否正确
4.判断端口号是否是一个数字
5.获取端口号
6.在启动web服务器时，使用制定的端口
"""

def main():
    # 2
    params_list = sys.argv
    # 3
    if len(params_list) != 2:
        print('启动失败，参数格式错误！正确格式:python3 xxxx.py 端口号')
        return

    # 4
    if not params_list[1].isdigit():
        print('启动失败，端口号必须为整数!')
        return

    # 5
    port = int(params_list[1])

    # 6在启动web服务器时，使用制定的端口

    ws = WebServer(port)
    ws.start()


if __name__ == '__main__':
    main()