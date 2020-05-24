import re
obj = re.compile(r'[Hello]')
mo = obj.findall('Hello')
print(mo)
                 
