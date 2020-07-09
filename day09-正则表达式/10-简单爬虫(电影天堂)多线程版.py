"""
@Author : Hirsi
@ Time :  2020/7/9
"""
import urllib.request
import re
import threading
import time


class MovieSpider(object):
    def __init__(self):
        # 定义i记录电影数
        self.i = 1
        # 定义一个字典，保存影片下载信息
        self.movie_dict = {}
        # 锁
        self.lock = threading.Lock()

    def strat(self):
        for i in range(1, 3):
            t1 = threading.Thread(target=self.get_MoviefInfo_links, args=(i,))
            # t1.setDaemon(True)
            t1.start()


        # 线程等于1是，说明多线程运行完退出了,所以不等于1，要无限循环，不运行下面的代码
        while len(threading.enumerate()) != 1:
            # time.sleep(3)
            pass

        a= 1
        # for name, url in self.movie_dict.items():
        #
        #     print(a,name,url)
        #     a+=1

        try:
            with open('movie url.txt', 'wb') as file:
                for name, url in self.movie_dict.items():
                    # 组成字符串，变成二进制写入文件
                    movieData=str(f'{a}.{name}\t{url}\n').encode()
                    file.write(movieData)
                    a+=1
        except Exception as ex:
            print('存储失败:',ex)
        else:
            print('存储成功!')


    def get_MoviefInfo_links(self, page):
        """获得电影详情页列表的函数"""
        # 1.定义列表页地址
        movie_list_url = f'https://www.ygdy8.net/html/gndy/dyzz/list_23_{page}.html'

        # 2.打开url地址，获取数据
        response_list = urllib.request.urlopen(movie_list_url)
        # 3.通过read()读取网络资源数据,并解码
        response_text = response_list.read().decode('GBK', 'ignore')

        # 4.使用正则得到所有影片的详情页地址
        info_url_list = re.findall('<a href="(.*?)" class="ulink">(.*?)</a>', response_text)

        # 4.1遍历url_list并拆包
        for info_url, movie_name in info_url_list:
            info_url = 'https://www.ygdy8.net/' + info_url
            """获取电影下载链接"""
            # 打开url地址，获取数据,通过read()读取网络资源数据,并解码
            movie_info_text = urllib.request.urlopen(info_url).read().decode('GBK', 'ignore')
            # movie_link = re.search('<a href="(ftp:.*?)">|href="(magnet:.*?)">', movie_info_text)
            movie_link = re.search('<a href="(ftp:.*?)">', movie_info_text)

            # 第一个正则没有，就检索下一个正则，有就取值
            if movie_link == None:
                movie_link = re.search('href="(magnet:.*?)">', movie_info_text)
                # 第二个正则如果也为空，就取值为‘无’或者跳过，继续循环，有就取值
                if movie_link == None:
                    group_data = '无'
                    # continue
                else:
                    group_data = movie_link.group(1)

            else:
                group_data = movie_link.group(1)

            # 在字典中添加影片信息
            self.lock.acquire()
            self.movie_dict[movie_name] = group_data
            print(self.i ,'条成功!')
            self.lock.release()

            self.i += 1

        # print(movie_dict)
        return self.movie_dict


def main():
    ms = MovieSpider()
    ms.strat()


if __name__ == '__main__':
    main()
