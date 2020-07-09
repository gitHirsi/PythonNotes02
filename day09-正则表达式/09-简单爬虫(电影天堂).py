"""
@Author : Hirsi
@ Time :  2020/7/7
"""

"""
一.定义函数，获取列表页的影片详情页的地址 get_movie_links()
    1.定义列表页地址 https://www.ygdy8.net/html/gndy/dyzz/list_23_1.html
    2.打开url地址，获取数据
    3.解码获取到的数据
    4.使用正则得到所有影片的详情页地址
    
二.主函数main
"""
import urllib.request
import re


def get_MoviefInfo_links():
    """获得电影详情页列表的函数"""
    # 定义i记录页数
    i = 1
    # 定义一个字典，保存影片下载信息
    movie_dict = {}
    while i <= 3:
        # 1.定义列表页地址
        movie_list_url = f'https://www.ygdy8.net/html/gndy/dyzz/list_23_{i}.html'

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
            if movie_link==None:
                movie_link = re.search('href="(magnet:.*?)">', movie_info_text)
                # 第二个正则如果也为空，就取值为‘无’或者跳过，继续循环，有就取值
                if movie_link==None:
                    # group_data = '无'
                    continue
                else:
                    group_data = movie_link.group(1)

            else:
                group_data = movie_link.group(1)

            print(movie_name, i, '>>>', group_data)
            # 在字典中添加影片信息
            movie_dict[movie_name] = group_data

        i += 1
    # print(movie_dict)
    return movie_dict


def main():
    movie_dict = get_MoviefInfo_links()
    # for name,url in movie_dict.items():
    #     print('>>>>>>>>>>>>>',name,url)


if __name__ == '__main__':
    main()
