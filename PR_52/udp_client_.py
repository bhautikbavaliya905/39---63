import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

c.sendto("Hello from UDP Client".encode(), ("localhost", 9999))

data, addr = c.recvfrom(1024)

print("Server:", data.decode())

c.close()

