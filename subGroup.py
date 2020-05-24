import re
obj = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')
mo = obj.search('192.168.11 0..0.0 1.1.1.1')
print(mo.group())
                 
