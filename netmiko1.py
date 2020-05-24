from netmiko import ConnectHandler
from datetime import datetime

cisco_3750={'device_type':'cisco_ios',
            'ip':'10.106.57.251',
            'username':'admin',
            'password':'cisco',}
net_connect=ConnectHandler(**cisco_3750)
print net_connect.find_prompt()

output = net_connect.send_command("show ip int br")
print output
