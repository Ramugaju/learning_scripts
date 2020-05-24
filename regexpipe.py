import re
regexObj = re.compile(r'Batman|Tina Fay')
mo1 = regexObj.search('Batman and Tina Fay')

print(mo1.group())

mo2 = regexObj.search('tina Fay and batman')
print(mo2)

print(mo2.group())



