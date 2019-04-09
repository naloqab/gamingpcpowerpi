import paramiko

ip = '192.168.1.210'
port = 22
username = 'naloqab'
password = os.environ["gaming_pc_password"]

command = 'shutdown -p'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)