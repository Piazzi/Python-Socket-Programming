import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 12000
MESSAGE = 4 + 4

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input(">")
    socket.sendto(data.encode('utf-8'), (UDP_IP, UDP_PORT))
    data, address = socket.recvfrom(2048)
    text = data.decode('utf-8')
    print('Received from server %s : %s ' % (address, text))
