import os, paramiko
from time import sleep

host = '192.168.1.210'
SSHPort = 22
username = 'naloqab'
password = os.environ["gaming_pc_password"]

logPath = '/home/pi/code/GamingPCPowerStatus.txt'

while True:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, SSHPort, username, password)

        PowerStatus = 'ON'

    except:
        PowerStatus = 'OFF'

    if not os.path.exists(logPath):
        os.system("touch {}".format(logPath))

    StatusFile = open(logPath, 'w')
    StatusFile.write(PowerStatus)
    StatusFile.close()

    sleep(10)