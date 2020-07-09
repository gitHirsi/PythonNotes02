import socket
import time

udp_so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
udp_so.bind(('', 12138))

# 设置广播权限
# udp_so.setsockopt(套接字，属性，属性值)
# socket.SOL_SOCKET  当前的套接字
# socket.SO_BROADCAST  广播属性
udp_so.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

# 发送信息
# udp_so.sendto('这是一条性感的广播信息！\n'.encode(),('255.255.255.255',8080))
for i in range(1, 10):
    udp_so.sendto(f'这是第{i}条广播信息！\n'.encode(), ('255.255.255.255', 8080))
    time.sleep(2)
    
udp_so.close()
