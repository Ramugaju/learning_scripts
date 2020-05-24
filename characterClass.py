import re
obj = re.compile(r'\S+')
mo = obj.findall('hello1_!')
print(mo)
