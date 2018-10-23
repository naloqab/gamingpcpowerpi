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
	try:
		print("\nWaiting for client to connect..\n")

		# script waits at this line until a client connects
		conn, Address = s.accept()

		print(Address, "is connected.")
		data = conn.recv(1024)
		print("Data received:", data, "\n", flush=True)

		command = data

		if command == b"GamingPCPowerStatus":
			statusFile = open("/home/pi/code/GamingPCPowerStatus.txt", 'r')
			GamingPCPowerStatus = statusFile.readline().strip()
			conn.send(GamingPCPowerStatus.encode('ascii'))
			print("Sending", str(command.decode("ascii")), "\n")

		else:
			os.system(command)
			print("Running", str(command.decode("ascii")), "\n")

	except Exception as e:
		print("Error:", str(e), flush=True)

	conn.close()
