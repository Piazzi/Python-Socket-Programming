# Python program to implement client side of chat room. 
import socket 
import select 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP = "127.0.0.1"
PORT = 3030

server.connect((IP, PORT)) 
print('Connected to the chat!')
print('Press [X] to close the connection')

while True: 
  
    serverMessage = server.recv(2048)
    print("<Fulano>")
    print(serverMessage.decode())

    if serverMessage == 'Bye!':
        break

    print("<You>") 
    message = input()
    if message == 'X':
        server.send('Bye!'.encode())
        break

    server.send(message.encode()) 

    print('\n')


    
server.close() 
print('Connection Closed')
