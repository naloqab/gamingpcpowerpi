import socket, time, os
from datetime import datetime

# emtpy host means localhost
Host = ''
Port = 5009

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((Host, Port))
    s.listen(1)
except Exception as e:
    print(str(datetime.now().strftime("%H:%M:%S")) + " - Error: " + str(e), flush=True)
    exit()

while True:
	try:
		print(str(datetime.now().strftime("%H:%M:%S")) + " - Waiting for client to connect..\n", flush=True)

		# script waits at this line until a client connects
		conn, Address = s.accept()

		print(str(datetime.now().strftime("%H:%M:%S")) + " - " + str(Address) + " is connected.\n", flush=True)
		data = conn.recv(1024)
		print(str(datetime.now().strftime("%H:%M:%S")) + " - Data received: " + str(data) + "\n", flush=True)

		command = data

		if command == b"GamingPCPowerStatus":
			statusFile = open("/home/pi/code/GamingPCPowerStatus.txt", 'r')
			GamingPCPowerStatus = statusFile.readline().strip()
			conn.send(GamingPCPowerStatus.encode('ascii'))
			print(str(datetime.now().strftime("%H:%M:%S")) + " - Sending " + str(command.decode("ascii")) + "\n", flush=True)

		else:
			os.system(command)
			print(str(datetime.now().strftime("%H:%M:%S")) + " - Running " + str(command.decode("ascii")) + "\n", flush=True)

	except Exception as e:
		print(str(datetime.now().strftime("%H:%M:%S")) + " - Error: " + str(e), flush=True)

	conn.close()
