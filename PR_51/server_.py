import socket

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP address and port
s.bind(("localhost", 9999))

# Listen for client
s.listen(1)

print("Waiting for client...")
conn, address = s.accept()

print("Client connected:", address)

# Server sends message
message = input("Server: ")
conn.send(message.encode())

# Receive message from client
message = conn.recv(1024).decode()
print("Client:", message)

# Close connection
conn.close()
s.close()

