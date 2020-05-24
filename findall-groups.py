import re
obj = re.compile(r'\d{1,3}(\w+)')
mo = obj.findall('123abc 456agbdvcg 12abc')
print(mo)
