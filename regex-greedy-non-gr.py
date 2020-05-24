import re
greedyReg = re.compile(r'(HA){3,5}')
mo = greedyReg.search('HAHAHAHAHAHAHAHA')
print(mo.group())

nongreedyReg = re.compile(r'(HA){7,8}?')
mo2 = nongreedyReg.search('HAHAHAHAHAHAHAHA')
print(mo2.group())
