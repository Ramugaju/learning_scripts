import netmiko
import getpass
import time
username = raw_input("Enter the username:")
password = getpass.getpass()

def connect_device(HOST):
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
    print(output)
    
    
