import re
obj = re.compile(r'\d{1,3}?')
mo = obj.findall("192.168")
print(mo)
