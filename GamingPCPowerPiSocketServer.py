import socket
import time
import os

# emtpy host means localhost
Host = ''
Port = 5009

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))
s.listen(1)

while True:
	print("\nWaiting for client to connect..\n")

	# script waits at this line until a client connects
	conn, Address = s.accept()

	print(Address, "is connected.")
	data = conn.recv(1024)
	print("Data received:", data, "\n")

	command = data

	os.system(command)

	conn.close()