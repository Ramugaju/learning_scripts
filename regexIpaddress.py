import re
obj = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
mo = obj.findall("My Ip addresses are 325.168.1.1,192.168.1.2.172.168.1.1.1.1.1.1")
print(mo)
