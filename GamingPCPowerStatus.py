import os
import paramiko

host = '192.168.1.200'
SSHPort = 22
username = 'naloqab'
password = 'Amber8599'

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, SSHPort, username, password)

    PowerStatus = 'ON'
    
except:
    PowerStatus = 'OFF'

logPath = 'GamingPCPowerStatus.txt'

if not os.path.exists(logPath):
    os.system("touch {}".format(logPath))

StatusFile = open(logPath, 'w')
StatusFile.write(PowerStatus)
StatusFile.close()