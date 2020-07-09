"""
@Author : Hirsi
@ Time :  2020/6/29
"""
"""
根据提供的状态和内容拼接http响应报文
"""

def creatr_http_response(status, response_body):
    # 拼接相应的报文
    response_line = f'HTTP/1.1 {status}\r\n'
    response_header = 'Server:Pythonws3.0\r\n'
    # 使用html语言进行解析
    response_header += 'Content-Type: text/html\r\n'
    response_blank = '\r\n'

    # 发送报文
    response_data = (response_line + response_header + response_blank).encode() + response_body
    return response_data
