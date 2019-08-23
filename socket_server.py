import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)



server.bind(('127.0.0.10',8000))

server.listen(1)

print("Waiting for client...")
client_o, c_addr = server.accept()
print("Client Address:",c_addr)

while True:
    data= client_o.recv(1024)
    if data.decode().lower()=='bye':
        client_o.send("Bye bye".encode())
        break
    print("Client->",data.decode('utf-8'))
##    client_o.send("Hi client".encode())
    client_o.send(input("Server:").encode())

server.close()
