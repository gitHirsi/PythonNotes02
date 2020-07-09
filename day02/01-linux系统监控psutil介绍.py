#!/usr/bin/python3.8
import psutil
import datetime
# 获取cpu的核心数
print(psutil.cpu_count(logical=False))
#2 CPU的使用率
print(psutil.cpu_percent(interval=0.5))
# 2.1获取每个核心的使用率
print(psutil.cpu_percent(interval=0.5,percpu=True))
# 3 获取内存信息
# 3.1 内存的整体信息
print(psutil.virtual_memory())
# 3.2内存的使用率
print(psutil.virtual_memory().percent)

# 4 获取硬盘信息
# 4.1获取硬盘的分区信息
print(psutil.disk_partitions())
# 4.2获取制定目录的磁盘信息
print(psutil.disk_usage('/'))
# 4.3硬盘的使用率
print(psutil.disk_usage('/').percent)

# 5 获取网络信息
# 5.1获取受到的数据包数量
print(psutil.net_io_counters().bytes_recv)
# 5.2获取发送的数据包数量
print(psutil.net_io_counters().bytes_sent)

# 6 获取开机时间
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S'))
# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%F %T'))

#获取系统当前时间
print(datetime.datetime.now().strftime('%F %T'))