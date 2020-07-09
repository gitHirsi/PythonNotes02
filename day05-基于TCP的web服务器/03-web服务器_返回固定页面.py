"""
@Author : Hirsi
@ Time :  2020/6/24
"""
"""
简单的web服务器_返回固定页面
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

    with open('static/index.html', 'rb') as file:
        response_body = file.read()

    response_data = (response_line + response_header + response_blank).encode()+response_body
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
