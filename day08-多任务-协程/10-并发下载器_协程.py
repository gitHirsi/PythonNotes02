"""
@Author : Hirsi
@ Time :  2020/7/6
"""

"""
main()
1.定义要下载的图片路径
2.调用文件下载的函数，专门下载文件

文件下载函数
1.根据url地址请求网络资源
2.在本地创建文件，准备保存
3.读取网络资源数据(while)
4.把读取的网络资源写入到本地文件中
5.异常捕获

打开网址 : urllib.request.urlopen(网址)
批量把协程添加join() : event.joinall([g1, g2, g3]) 
"""
from gevent import monkey

monkey.patch_all()

import urllib.request
import gevent
import time

startTime = time.time()


def downloadImg(imgUrl, file_name):
    # 异常捕获
    try:
        # 根据url地址请求网络资源(返回值是二进制数据)
        response_data = urllib.request.urlopen(imgUrl)
        # 在本地创建文件，准备保存
        with open(file_name, 'wb') as f:
            while True:
                # 读取网络资源数据
                file_data = response_data.read()
                if file_data:
                    # 把读取的网络资源写入到本地文件中
                    f.write(file_data)
                else:
                    break
    except Exception as ex:
        print(f"'{file_name}'下载失败:",ex)
    else:
        print(f"'{file_name}'下载成功")




def main():
    # 定义要下载的图片路径
    img_url1 = "http://img.mp.itc.cn/upload/20170716/8e1b835f198242caa85034f6391bc27f.jpg"
    img_url2 = "http://img.mp.sohu.com/upload/20170529/d988a3d940ce40fa98ebb7fd9d822fe2.png"
    img_url3 = "http://image.uczzd.cn/11867042470350090334.gif?id=0&from=export"
    # 调用文件下载的函数，专门下载文件
    # downloadImg(img_url1, '1.gif')
    # downloadImg(img_url2, '2.gif')
    # downloadImg(img_url3, '3.gif')


    # 创建协程方式下载
    g1 = gevent.spawn(downloadImg, img_url1, '1.gif')
    g2 = gevent.spawn(downloadImg, img_url2, '2.gif')
    g3 = gevent.spawn(downloadImg, img_url3, '3.gif')
    #  批量把协程给join()
    gevent.joinall([g1, g2, g3])


if __name__ == '__main__':
    main()

    endTime = time.time()
    # 记录程序运行时间
    runTime=endTime - startTime
    print(runTime)