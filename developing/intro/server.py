import socket

server = socket.socket()

server.bind(('127.0.0.1', 8000)) 
#              ^
# start server |
server.listen()

client, address_cl = server.accept()

print(address_cl)

while True:
    msg = client.recv(1024).decode()
    if msg == 'q':
        break
    print(msg)

server.close()