import socket

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

addr= ('127.0.0.10',8000)

client.connect(addr)

while True:
    client.send(input("Client:").encode())
    data= client.recv(1024)
    if data.decode()=='Bye bye':
        break
    print("Server->",data.decode())

client.close()
