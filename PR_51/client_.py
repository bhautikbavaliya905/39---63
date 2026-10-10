import socket

# Create socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
c.connect(("localhost", 9999))

# Receive message from server
message = c.recv(1024).decode()
print("Server:", message)

# c sends message
message = input("Client: ")
c.send(message.encode())

# Close connection
c.close()