# Python program to implement client side of chat room. 
import socket 
import select 
  
IP = "127.0.0.1"
PORT = 3030

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.connect((IP, PORT)) 
print('Connected to the chat!')
print('Press [X] to close the connection \n')

while True: 
  
    socketMessage = socket.recv(2048)
    print("<Fulano>")
    print(socketMessage.decode() + '\n')
    if socketMessage.decode() == 'Bye!':
        break

    print("<You>") 
    message = input(">")
    if message == 'X':
        socket.send('Bye!'.encode())
        break
    print('\n')
    socket.send(message.encode()) 


socket.close() 
print('Connection Closed')
