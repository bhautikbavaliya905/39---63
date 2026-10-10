import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(("localhost", 9999))

c.send("Hello from Client".encode())

message = c.recv(1024).decode()
print("Server says:", message)

c.close()
