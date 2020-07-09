# 1.导入模块
import socket

# 2.创建套接字  TCP
tcp_client_so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client_so.bind(('',12138))

# 3.建立连接   connect()
# tcp_client_so.connect(address)
# address=('ip',端口)
tcp_client_so.connect(('192.168.1.2', 8080))

# 4.发送数据
tcp_client_so.send('你还好吗？'.encode())

# 5.接受数据    返回的就是法服务端回复信息的二进制
recv_data = tcp_client_so.recv(1024)
print(recv_data)
print(recv_data.decode('GBK'))

# 6.关闭套接字
tcp_client_so.close()
