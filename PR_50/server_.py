import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 9999))
s.listen(1)

print("Server is waiting for connection...")

conn, addr = s.accept()
print("Connected with:", addr)

message = conn.recv(1024).decode()
print("Client says:", message)

conn.send("Hello from Server".encode())

conn.close()
s.close()
