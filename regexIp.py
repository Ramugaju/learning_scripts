import re
regexObj = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = regexObj.search("This is my phone number:455-525-4523")
print('Phone number found:'+mo.group())
                     
