import socket

def send_file_2_client(new_client_socket, client_addr):
    file_name = new_client_socket.recv(1024).decode()
    if file_name == 'exit':
        print("退出系统。")
        return "exit"
    print(f"客户端{str(client_addr)}需要下载的文件是：{file_name}")
    file_content = None
    try:
        with open(file_name, 'rb') as f:
            file_content = f.read()
    except Exception as e:
        print(f"没有找到需要下载的文件{file_name}")
        return False
    if file_content:
        new_client_socket.send(file_content)
        return True
    else:
        print("文件为空")
        return False


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口可修改
    local_addr = ("", 7788)
    tcp_server_socket.bind(local_addr)
    tcp_server_socket.listen(128)
    cnt = 0
    while True:
        new_client_socket, client_addr = tcp_server_socket.accept()
        if not cnt:
            print("客户端连接成功，您最多可以发送8个文件，输入exit以终止收发。！")
        flg = send_file_2_client(new_client_socket, client_addr)
        if flg == "exit":
            break
        if flg and flg != "exit":
            cnt += 1
        new_client_socket.close()
        if cnt == 8:
            break

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
