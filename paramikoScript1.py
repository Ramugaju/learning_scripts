import paramiko
import time
import getpass

user = raw_input("Enter the username:")
password = getpass.getpass()


def ssh_to_ip(ip):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname = ip,username =user,password = password)
    print("Successful connection "+ip)
    remote_connection = ssh_client.invoke_shell()
    remote_connection.send("enable\n")
    remote_connection.send("cisco\n")
    remote_connection.send("config terminal\n")
    for i in range(1,11):
        remote_connection.send("vlan "+str(i)+"\n")
        remote_connection.send("name python_vlan"+str(i)+"\n")
        time.sleep(0.5)
    remote_connection.send("end\n")
    time.sleep(1)
    output = remote_connection.recv(65535)
    print(output)

f = open("/root/ip-address-file.txt")

for eachline in f:
    HOST = eachline.strip()
    ssh_to_ip(HOST)
