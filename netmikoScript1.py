#!/usr/bin/env python

from netmiko import connectHandler

user = raw_input("Enter the username:")
password = getpass.getpass()

HOST = 192.168.122.41

iosv_l2 = {
    'device_type':'cisco_ios',
    'ip': HOST,
    'username':user,
    'password':password,
    }

net_connect = connectHandler(**iosv_l2)

output = net_connect.send_command('show ip int brief')
print(output)
