import paramiko
import time
import getpass
import os
import datetime
import telnetlib
#from termcolor import colored
## The following three lines will create a folder with the name appended with Date and timestamp##
## Outputs collected from individual switches are saved in this folder##
path = "/home/ramugajula/config-logs"
mydir = os.path.join(path , datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(mydir)

##################################################
devices = "/home/ramugajula/devices.txt"
config = "/home/ramugajula/config.txt"

##################################################
# Following two lines will ask for your credentials to loginto switches. #
#Creds should have privilege access 15 #
user = input("Enter the username:")
password = getpass.getpass()

# Function to login to switch to  collect show commands output and save to a text file#
def ssh_to_ip(ip):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname = ip,username =user,password = password)
    print("Successful connection to....."+ip)
    remote_connection = ssh_client.invoke_shell()
    conf_file = open("/home/ramugajula/config.txt")
    for line in conf_file:
        command = line.strip()+"\n"
        remote_connection.send(command.encode('ascii'))
        #remote_connection.send(\n.encode('ascii'))
        time.sleep(1)
    output = (remote_connection.recv(65535)).decode('ascii')
    print(output)
    output_file = open("{}/{}.txt".format(mydir,ip),'w')
    output_file.write(output)
def telnet_to_ip(HOST):

    tn = telnetlib.Telnet(HOST,timeout = 2)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    print ("Telnet session established with " + (HOST))
    conf_file = open("/home/ramugajula/config.txt")
    for each_line in conf_file:
        command = eachline.strip()
        tn.write(command.encode('ascii'))
    print(tn.read_all())
    log_output = tn.read_all()
    saveoutput = open("{}/{}.txt".format(mydir,HOST),'w')
    saveoutput.write(log_output.decode('ascii'))
    saveoutput.write("\n")
    print("Output saved to file {}.txt".format(HOST))
    time.sleep(1)
# Following line will open a text file where your Ip address inventory is saved.#
f = open("/home/ramugajula/devices.txt")
# The following code iterates through your ip inventory file line by line.#
# Takes the ip address and calls the abive function, passing the IP address as argument#
for eachline in f:
   HOST = eachline.strip()
   try:
      ssh_to_ip(HOST)
   except paramiko.ssh_exception.NoValidConnectionsError:
      print("cannot SSH {}, Trying Telnet now...!".format(HOST))
      try:
          telnet_to_ip(HOST)
      except:
          print("Telnet to {} failed as well..It's time for you to troubleshoot!".format(HOST))
          print("Proceeding to next Ip address in the list!")
          print("!")
          print("!")
          continue
