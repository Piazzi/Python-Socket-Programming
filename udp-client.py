import socket

IP = "127.0.0.1"
PORT = 12000

print('Welcome to the simple calculator! \n - Press X if you want to exit \n - Insert the values of A and B and then the operation you want to make')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    print('Insert the value for A')
    a = input()

    print('Insert the value for B')
    b = input()

    print('Insert the arithmetic operation')
    operator = input()



    message = a +', '+b+', '+operator
    print('Message being send to server: ' + message + "\n")

    socket.sendto(message.encode('utf-8'), (IP, PORT))
    if a == 'X' or b == 'X' or operator == 'X':
        break

    data, address = socket.recvfrom(2048)
    text = data.decode('utf-8')
    print('Result received from server %s : %s ' % (address, text) + "\n")

print('Connection Closed')
socket.close()
