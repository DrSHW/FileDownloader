import socket

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ip和端口可以自己设置
    tcp_address = ('192.168.43.157', 7788)
    print("正在连接服务器...")
    tcp_socket.connect(tcp_address)
    print("连接成功")
    cnt = 8
    while cnt:
        download_file_name = input('请输入要下载的文件名：')
        tcp_socket.send(download_file_name.encode('utf-8'))
        recv_data = tcp_socket.recv(1024)
        if recv_data:
            with open("[new]" + download_file_name, 'wb') as f:
                f.write(recv_data)
            print('下载成功')
            cnt -= 1
    tcp_socket.close()
if __name__ == '__main__':
    main()