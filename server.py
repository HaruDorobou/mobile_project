import socket
import os

IP = '127.0.0.1'  # '192.168.219.174'
PORT = 8000


def receive_file(conn):
    file_name_1 = conn.recv(1024).decode()
    print(file_name_1)

    if file_name_1 == 'send protocol end':
        conn.close()
        return 0

    nowdir = os.getcwd()
    desdir = os.path.join(nowdir, 'data')
    data_transferred = 0
    with open(desdir + "\\" + file_name_1, 'wb') as f:  # 현재dir에 filename으로 파일을 받는다
        try:
            data = conn.recv(1024)
            while data:  # 데이터가 있을 때까지
                if data == b'EOF':
                    break
                f.write(data)  # 1024바이트 쓴다
                data_transferred += len(data)
                data = conn.recv(1024)  # 1024바이트를 받아 온다
        except Exception as ex:
            print(ex)
    print('파일 %s 받기 완료. 전송량 %d' % (file_name_1, data_transferred))
    return 1


def make_server_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, int(PORT)))
    s.listen(1)
    print("server socket was created")
    return s


if __name__ == '__main__':
    server_socket = make_server_socket()
    conn1, addr = server_socket.accept()
    print('Connection address : ' + str(addr))
    s = 1
    while s:
        conn1.send('ready'.encode())
        s = receive_file(conn1)

