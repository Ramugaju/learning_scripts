import re
regexObj = re.compile(r'Bat(man|Tina|women)')
mo1 = regexObj.search('Batman and Tina Fay Batwomen')
print(mo1.group())
