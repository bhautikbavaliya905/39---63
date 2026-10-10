import socket

c = socket.socket()
c.connect(("localhost", 9999))

filename = input("Enter file name: ")

c.send(filename.encode())

data = c.recv(100000)

with open("downloaded_" + filename, "wb") as file:
    file.write(data)

print("File downloaded successfully")

c.close()

