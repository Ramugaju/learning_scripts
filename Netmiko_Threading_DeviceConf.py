import re
import getpass
#import paramiko
import netmiko
import time
import sys
#import ipaddress
import threading


f = open('/users/ramugaju/documents/regexfile.txt')


extracted_ips = []
for line in f:
    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line):
        mo = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",line)
        for i in mo:
            extracted_ips.append(i)
    else:
        print("No ip addresses found in the file")

print(extracted_ips)
f.close()

def split(ip):
    splitList = ip.split(".")
    #print(splitList)
    for i in range(len(splitList)):
        if int(splitList[i]) > 255:
            #print(ip+" is invalid")
            return False
            break
        else:
            continue
    return True

valid_ips = []
for each_ip in extracted_ips:
    print(each_ip)
    if split(each_ip):
        valid_ips.append(each_ip)
    else:
        print(each_ip+" is not a valid IP\n")

print("final valid ip's are :\n")
print(valid_ips)

print("""

Now we will use threading to connect all the valid Ip's concurrently and

do the job.

""")

username = raw_input("Enter the username to connect to device:")
password = getpass.getpass()

def connect_device(n,HOST):
    from netmiko import ConnectHandler
    iosv_l2 = {
    'device_type':'cisco_ios',
    'ip': HOST,
    'username':username,
    'password':password,
    }
    net_connect = ConnectHandler(**iosv_l2)
    config_commands = ['username script1 password script']
    output = net_connect.send_config_set(config_commands)
    time.sleep(n)
    print(output)

threads_list = []
for i in range(len(valid_ips)):
    t = threading.Thread(target = connect_device,name = "Thread open for {}".format(valip_ips[i])
                         args = (5, valid_ips[i]))
    threads_list.append(t)

for t in threads_list:
    t.start()
