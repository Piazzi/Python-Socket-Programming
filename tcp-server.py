# Python program to implement socket side of chat room. 
import socket 

IP = "127.0.0.1"
PORT = 3030

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind((IP, PORT)) 
socket.listen(1) 

print('Waiting for someone to enter the chat...')
connectionSocket, address = socket.accept()
print('Someone entered in the chat, say something! \n')

while True:

    print("<You>") 
    yourMessage = input(">")
    print('\n')
    if yourMessage == 'X':
        connectionSocket.send('Bye!'.encode())
        break
    connectionSocket.send(yourMessage.encode())

    messageReceived = connectionSocket.recv(2048)
    print('<Fulano>')
    print(messageReceived.decode() + '\n')
    if messageReceived.decode() == 'Bye!':
        break
    

socket.close()
print('Connection Closed')


