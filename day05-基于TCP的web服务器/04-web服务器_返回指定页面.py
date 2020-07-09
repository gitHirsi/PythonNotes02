"""
@Author : Hirsi
@ Time :  2020/6/24
"""
"""
简单的web服务器_返回制定页面
注重:1.根据客户端浏览器请求的资源路径，返回请求资源
     2.只输入地址，默认访问index.html(设主页)
     3.访问的页面不存在处理方法
"""
import socket as so


def request_headler(new_client_so, ip_port):
    recv_data = new_client_so.recv(1024)
    if not recv_data:
        print(f'客户端{ip_port}已下线')
        new_client_so.close()
        return

    # 拼接相应的报文
    response_line = 'HTTP/1.1 200 OK\r\n'
    response_header = 'Server:Pythonws2.012\r\n'
    response_blank = '\r\n'

    # ***根据客户端浏览器请求的资源路径，返回请求资源***
    # 1) 把请求协议解码，得到请求报文的字符串
    request_text = recv_data.decode()
    # 2) 得到请求行
    # 2.1查找第一个 \r\n 出现的位置
    loc = request_text.find('\r\n')
    # 2.2 截取字符串，从头开始截取到第一个 \r\n 出现的位置
    request_line = request_text[:loc]
    # 3) 把请求行，按照空格拆分，得到列表
    rl_list = request_line.split(' ')
    print(rl_list)
    # 页面的路径
    html_path = rl_list[1]

    # ***只输入地址，默认访问index.html***
    if html_path == '/':
        html_path='/index.html'

    # 读取文件，传送给客户端
    # ***访问的页面不存在处理方法***
    try:
        with open('static' + html_path, 'rb') as file:
            response_body = file.read()
    except Exception as ex:
        response_line='HTTP/1.1 404 Not Found\r\n'
        response_body=('Error!'+str(ex)).encode()


    response_data = (response_line + response_header + response_blank).encode() + response_body
    new_client_so.send(response_data)

    new_client_so.close()


def main():
    tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)

    tcp_server_so.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, True)

    tcp_server_so.bind(('', 12138))

    tcp_server_so.listen(128)

    while True:
        new_client_so, ip_port = tcp_server_so.accept()
        print(f'客户端{ip_port}上线了~')
        request_headler(new_client_so, ip_port)


if __name__ == '__main__':
    main()
