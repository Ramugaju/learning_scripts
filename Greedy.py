import re
greedyObj = re.compile(r'(Ha){3,5}?')
mo = greedyObj.search('HaHaHaHaHaHa')

print(mo.group())
                       
