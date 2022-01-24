import socket

sock = socket.socket()
sock.connect(("81.200.31.248", 9000))

sock.send("some text data".encode())
data = sock.recv(10)
data = data.decode("utf8")
