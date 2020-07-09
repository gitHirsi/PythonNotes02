"""
@Author : Hirsi
@ Time :  2020/7/6
"""
from gevent import monkey
monkey.patch_all()

import socket as so
import sys
from application import app
import gevent

"""
1.在类的初始化方法中配置当前的项目
2.给类增加一个初始化项目配置方法 init_projects()
    2.1 显示所有可以发布的游戏 菜单
    2.2 接受选择，并发布选择的项目（保存选择的游戏对应的本地目录）
3.更改web服务器打开的文件目录
"""


class WebServer(object):
    def __init__(self, port):
        tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
        # 设置地址重用
        tcp_server_so.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, True)
        tcp_server_so.bind(('', port))
        tcp_server_so.listen(128)

        # 定义实例属性，保存套接字对象
        self.tcp_server_so = tcp_server_so
        self.current_dir = ''

        self.projects_dict = dict()
        self.projects_dict['植物大战僵尸-普通版'] = "zwdzjs-v1"
        self.projects_dict['植物大战僵尸-外挂版'] = "zwdzjs-v2"
        self.projects_dict['保卫萝卜'] = "tafang"
        self.projects_dict['2048'] = "2048"
        self.projects_dict['读心术'] = "dxs"

        # 调用初始化项目的方法
        self.init_projects()

    # 2 .添加一个初始化项目的方法
    def init_projects(self):
        # 2.1 显示所有可以发布的游戏菜单
        keys_list = list(self.projects_dict.keys())
        # 便利所有key
        for index, game_name in enumerate(keys_list):
            print(f'{index + 1}.{game_name}')
        # 2.2 接受选择，并发布选择的项目（保存选择的游戏对应的本地目录）
        game_num = int(input('请选择游戏发布:'))
        key = keys_list[game_num - 1]

        # 根据字典的key得到项目的路径
        self.current_dir = self.projects_dict[key]

    def start(self):
        """ 启动web服务器"""
        print('服务器启动成功...')
        while True:
            new_client_so, ip_port = self.tcp_server_so.accept()
            print(f'客户端{ip_port}已连接~~')

            #***创建协程,分派任务***
            gevent.spawn(self.request_headler, new_client_so, ip_port)
            #主线程一直在循环，没有退出，所以不需要join()


    # 接受客户端浏览器发送的请求协议
    def request_headler(self, new_client_so, ip_port):
        request_data = new_client_so.recv(1024)
        if not request_data:
            print(f'客户端{ip_port}已断开~~')
            new_client_so.close()
            return

        # 调用app模块
        response_data = app.application(self.current_dir, request_data)
        print(request_data)

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