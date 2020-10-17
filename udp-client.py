import socket

IP = "127.0.0.1"
PORT = 12000

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:

    print('Insert the value for A')
    a = input()

    print('Insert the value for B')
    b = input()

    print('Insert the arithmetic operation')
    operator = input()

    message = a +', '+b+', '+operator
    print('Message being send to server: ' + message)
    print("\n")

    socket.sendto(message.encode('utf-8'), (IP, PORT))
    data, address = socket.recvfrom(2048)
    text = data.decode('utf-8')
    print('Result received from server %s : %s ' % (address, text))
    print("\n")
