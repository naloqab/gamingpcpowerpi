import paramiko

ip = '192.168.1.210'
port = 22
username = 'naloqab'
password = 'Amber8599'

command = 'shutdown -p'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)

# import os
# os.system("python3 /home/pi/code/GamingPCPowerButton.py 1")
