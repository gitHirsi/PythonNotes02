# 1、导入模块
import socket
# 2、创建套接字
# socket.socket(协议类型,传输方式)
# 参数一：
# socket.AF_INET 使用IPv4
# socket.AF_INET6 使用IPv6
# 参数二：
# socket.SOCK_DGRAM 使用UDP的传输方式（无连接）
# socket.SOCK_STREAM 使用TCP的传输方式（有连接）
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3、数据传输

# 4、关闭套接字
udp_socket.close()
