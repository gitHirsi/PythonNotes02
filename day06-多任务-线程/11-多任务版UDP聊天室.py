"""
@Author : Hirsi
@ Time :  2020/7/1
"""

import socket as so
import threading


def send_msg(udp_so):
    """发送消息的函数"""
    ip = input('请输入对方的IP地址:')
    if len(ip) == 0:
        ip = '192.168.1.5'
        print(f'默认接收方ip地址:{ip}')
    port = input('请输入对方的端口号:')
    if len(port) == 0:
        port = '12138'
        print(f'默认接收方端口为:{port}')
    content = input('请输入发送的消息:')
    udp_so.sendto(content.encode(), (ip, int(port)))


def recv_msg(udp_so):
    """接受消息的函数"""
    while True:
        recv_con, ip_port = udp_so.recvfrom(1024)
        print(f'来自{ip_port}的:{recv_con.decode("GBK")}')


def main():
    udp_so = so.socket(so.AF_INET, so.SOCK_DGRAM)
    # 绑定端口
    udp_so.bind(('', 12138))

    # 创建子线程,单独接受用户发送的信息
    t1 = threading.Thread(target=recv_msg, args=(udp_so,))
    # ***守护线程***
    t1.setDaemon(True)
    t1.start()

    while True:
        print('\n******************************')
        print('********  1.发送消息  ********')
        print('********  2.退出系统  ********')
        print('******************************')
        sel_num = int(input('请输入选项:\n'))
        if sel_num == 1:
            send_msg(udp_so)
        elif sel_num == 2:
            print('系统已退出')
            break
            # exit()
        else:
            print('选择无效！')
            main()
    udp_so.close()


if __name__ == '__main__':
    main()
