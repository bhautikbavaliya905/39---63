import socket

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)

print("File server is waiting...")

conn, addr = s.accept()
print("Client connected")

filename = conn.recv(1024).decode()

try:
    with open(filename, "rb") as file:
        data = file.read()
        conn.sendall(data)

    print("File sent successfully")

except FileNotFoundError:
    conn.send(b"File not found")

conn.close()
s.close()
