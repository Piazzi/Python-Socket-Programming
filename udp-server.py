import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 12000

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.bind((UDP_IP, UDP_PORT))

print('Listening At {}'.format(socket.getsockname()))

while True:
    msg_bytes, address = socket.recvfrom(2048)
    msg_str = msg_bytes.decode('utf-8')
    print('Received from client {} : {}'.format(address, msg_str))
    socket.sendto(msg_str.upper().encode(), address)