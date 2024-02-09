import socket

client = socket.socket()

client.connect(('127.0.0.1', 8000))

while True:
    msg = input('youre msg:')
    client.send(msg.encode())
    if msg == 'q':
        break

client.close()