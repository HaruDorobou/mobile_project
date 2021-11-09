from os.path import exists
import socket
import os
import time

IP = '127.0.0.1'  # '192.168.219.174'
PORT = 8000

file_name = ['accounts.notifications.db', 'build.prop', 'calendar.db',
             'calllog.db', 'contacts2.db', 'mmssms.db',
             'persistent_properties', 'WifiConfigStore.xml']


def send_file(socket, file_name):

    nowdir = os.getcwd()
    desdir = os.path.join(nowdir, 'data_send')

    if exists(desdir + "\\" + file_name):
        print('file exist')
        socket.send(file_name.encode())
        print("파일 %s 전송 시작" % file_name)

        data_transferred = 0
        time.sleep(0.1)
        with open(desdir + "\\" + file_name, 'rb') as f:
            try:
                data = f.read(1024)  # 1024바이트 읽는다
                while data:  # 데이터가 없을 때까지
                    data_transferred += socket.send(data)  # 1024바이트 보내고 크기 저장
                    data = f.read(1024)  # 1024바이트 읽음
            except Exception as ex:
                print(ex)
        print("전송완료 %s, 전송량 %d" % (file_name, data_transferred))
        socket.send(b'EOF')

    return


def make_client_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, int(PORT)))
    print("receiver socket was created")
    return s


if __name__ == '__main__':
    client_socket = make_client_socket()

    for file in file_name:
        data = client_socket.recv(1024)
        print(data.decode())
        send_file(client_socket, file)

    client_socket.send('send protocol end'.encode())

