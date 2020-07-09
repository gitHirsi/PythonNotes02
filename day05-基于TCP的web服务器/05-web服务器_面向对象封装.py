"""
@Author : Hirsi
@ Time :  2020/6/24
"""
"""
简单的web服务器_面向对象封装
"""
import socket as so


class WebServer(object):
    def __init__(self):
        tcp_server_so = so.socket(so.AF_INET, so.SOCK_STREAM)
        # 设置地址重用
        tcp_server_so.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, True)
        tcp_server_so.bind(('', 12138))
        tcp_server_so.listen(128)

        # 定义实例属性，保存套接字对象
        self.tcp_server_so = tcp_server_so

    def start(self):
        """ 启动web服务器"""
        while True:
            new_client_so,ip_port = self.tcp_server_so.accept()
            print(f'客户端{ip_port}已连接~~')
            self.request_headler(new_client_so,ip_port)

    #接受客户端浏览器发送的请求协议
    def request_headler(self,new_client_so,ip_port):
        request_data = new_client_so.recv(1024)
        if not request_data:
            print(f'客户端{ip_port}已断开~~')
            new_client_so.close()
            return

        # 拼接相应的报文
        response_line='HTTP/1.1 200 OK\r\n'
        response_header='Server:Pythonws3.0\r\n'
        response_blank='\r\n'

        #得到文件路径
        # 把请求协议解码，得到请求报文的字符串
        request_text = request_data.decode()
        loc = request_text.find('\r\n')
        request_line=request_text[:loc]
        # 把请求行，按照空格拆分，得到列表 ，并用下标得到html路径
        html_path=request_line.split(' ')[1]

        print(html_path)

        # 设置默认主页
        if html_path=='/':
            html_path='/index.html'

        try:
            with open('static'+html_path,'rb') as f:
                response_body = f.read()
        except Exception as ex:
            response_line='HTTP/1.1 4.4 Not Found\r\n'
            response_body=('Error!'+str(ex)).encode()

        #发送报文
        response_data=(response_line+response_header+response_blank).encode()+response_body
        new_client_so.send(response_data)

        new_client_so.close()

def main():
    ws = WebServer()
    ws.start()


if __name__ == '__main__':
    main()
