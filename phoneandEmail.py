import re

phoneObj = re.compile(r'(\d{3}|\(\d{3}\))?(-|\.)?(\d{3})(-|\.)?(\d{4})')
mo = phoneObj.search('my phone is: (455)5554532')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group(4))
print(mo.group(5))
