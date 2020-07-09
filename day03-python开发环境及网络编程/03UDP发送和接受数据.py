import socket as so

# 1.创建套接字
udp_so = so.socket(so.AF_INET, so.SOCK_DGRAM)
# 2.发送数据
# udp_socket.sendto(要发送的数据的二进制格式，对方的ip地址和端口号)
# 注：要求ip地质和端口要要组成一个元组，端口是整数类型
mes='Python vs Java'.encode()
udp_so.sendto(mes,('192.168.1.2',8080))
# 3.接受数据
# 每次接收1024个字节,返回的是一个元组
recv_data = udp_so.recvfrom(1024)
print(recv_data)
# recv_data 是一个元组
# 1第一个元素  收到的数据的二级制
# 2第二个元素  元组,发送方的ip和端口

# 把接收的数据解码   二进制 转换成 字符串
str1 = recv_data[0].decode("GBK")
# * 解码失败的处理   ignore:忽略   strict:严格
# str1 = recv_data[0].decode(encoding="UTF-8",errors='ignore')

print(f'来自{recv_data[1]}的：{str1}')

# 4.关闭套接字
udp_so.close()