import socket

# Create socket
s = socket.socket()

# Bind socket
s.bind(('localhost', 9999))

# Listen for connection
s.listen(1)

print("Waiting for connection...")

# Accept connection
conn, addr = s.accept()

print("Connected with:", addr)

# Send message
conn.send("Hello from server".encode())

# Close connection
conn.close()
s.close()

