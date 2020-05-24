import re
obj = re.compile(r'.at')
mo = obj.findall('The cat in the hat sat on the flat mat.')
print(mo)

for i in mo:
    print(i)
