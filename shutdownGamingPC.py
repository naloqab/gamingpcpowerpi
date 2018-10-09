#!/usr/bin/python3

import paramiko

ip = '192.168.1.200'
port = 22
username = 'naloqab'
password = 'Amber8599'

# command = 'ipconfig | findstr IPv4'
command = 'shutdown -p'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
# outputList = stdout.readlines()
# output = "\n".join(outputList)

# print(output)