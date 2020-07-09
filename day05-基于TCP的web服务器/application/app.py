"""
@Author : Hirsi
@ Time :  2020/6/29
"""
"""
处理并获得文件路径
"""

from application import utils


def parse_request(request_data):
    """解析请求的报文,返回客户端请求的资源路径"""
    # 得到文件路径
    # 把请求协议解码，得到请求报文的字符串
    request_text = request_data.decode()
    loc = request_text.find('\r\n')
    request_line = request_text[:loc]
    # 把请求行，按照空格拆分，得到列表 ，并用下标得到html路径
    html_path = request_line.split(' ')[1]

    # 设置默认主页
    if html_path == '/':
        html_path = '/index.html'

    return html_path

# 1
def application(current_dir, request_data):
    # 调用...
    html_path = parse_request(request_data)
    file_path = current_dir + html_path
    # print(file_path)

    try:
        with open(file_path, 'rb') as f:
            response_body = f.read()
            response_data = utils.creatr_http_response('200 OK', response_body)
    except Exception as ex:
        response_body = ('Error! ' + str(ex)).encode()
        response_data = utils.creatr_http_response('404 Not Found', response_body)

    return response_data
