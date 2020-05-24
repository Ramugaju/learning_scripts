import ipaddress
import re

def valid_ip(address):
    try: 
        print(ipaddress.ip_address(address))
        return True
    except:
        return False



obj = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
mo = obj.findall("My Ip addresses are 325.168.1.1,192.168.1.2.172.168.1.1.1.1.1.1")
print(mo)

valid_Ip = [1,2]
for i in mo:
    if valid_ip(i):
        #valid_Ip.append[i]
        #print(i+' is a valid ip')

print(valid_Ip)
