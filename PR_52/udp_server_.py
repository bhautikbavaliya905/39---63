import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("localhost", 9999))

print("UDP server is waiting...")

data, addr = s.recvfrom(1024)

print("Client:", data.decode())

s.sendto("Hello from UDP server".encode(), addr)

s.close()

