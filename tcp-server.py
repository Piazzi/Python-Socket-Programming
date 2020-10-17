# Python program to implement server side of chat room. 
import socket 

IP = "127.0.0.1"
PORT = 3030

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((IP, PORT)) 
server.listen(1) 

print('Waiting for someone to enter the chat...')
connectionSocket, address = server.accept()
print('Someone entered in the chat, say something!')

while True:

    print("<You>") 
    yourMessage = input()

    if yourMessage == 'X':
        server.send('Bye!'.encode())
        break

    print('\n')    

    connectionSocket.send(yourMessage.encode())
    messageReceived = connectionSocket.recv(2048)
    print('<Fulano>')
    print(messageReceived.decode())

    if messageReceived == 'Bye!':
        break


    
connectionSocket.close()
print('Connection Closed')


