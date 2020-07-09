import socket

udp_so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
# udp_so.bind(address)
# address是一个元组，🗼它的第一个元素是字符串类型的ip地址，第二个元素是整数端口
udp_so.bind(('',12138))

# 发送数据
udp_so.sendto('哈哈，我来了！\n'.encode(),('192.168.1.2',8080))
# 接受数据  返回的是元组，用拆包接受
recv_data ,ip= udp_so.recvfrom(1024)
# 解码
mes = recv_data.decode("GBK")
print(f'来自{ip}的:{mes}')

udp_so.close()
