import socket as so

# 创建套接字
udp_so = so.socket(so.AF_INET, so.SOCK_DGRAM)
# 绑定端口
# ip地址尽量写为'',好处是当计算机有多个网卡的时候，不同网卡的数据都能接收
udp_so.bind(('',12138))

# 接受数据，每次接受1024，并转码显示
recv_data,ip = udp_so.recvfrom(1024)
print(f"来自{ip}的:\n{recv_data.decode('GBK')}")

# 关闭套接字
udp_so.close()