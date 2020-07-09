
# 1.导入模块
import socket as so
# 2.创建套接字
tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
# 3.绑定端口
tcp_server_so.bind(('',12138))

# 4.开启监听
# listen（） ：设置套接字为被动监听模式，不能再主动发送数据了
# 128 ： 允许接受的最大连接数 ，在windows 128 有效，在linux下，此数字无效
tcp_server_so.listen(128)

# 5.等待客户端连接
# accept（）  开始接受客户端的连接,程序默认进入阻塞状态（等待客户端连接中）
# recv_data = tcp_server_so.accept()
# recv_data : 是个元组，有两个元素  （新的套接字，（‘ip’,端口））  所以可以拆包⬇
#     1)是返回了一个新的套接字socket
#     2）客户端的ip地址和端口号
new_client_so,client_ip_port = tcp_server_so.accept()
print(f'新客户端来了{client_ip_port}')

# 6.收发数据
# recv() 会让程序再次阻塞,受到信息，解除阻塞
new_client_so.send('已连接到服务器...'.encode())

recv_cont = new_client_so.recv(1024)
print(f"来自{client_ip_port}的：{recv_cont.decode('GBK')}")

new_client_so.close()   #表示不能再和当前客户端通信了

# 7.关闭套接字
tcp_server_so.close()  #表示程序不再接受新的客户端连接,已经连接的可以继续服务

