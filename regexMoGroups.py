import re
regexObj = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = regexObj.search("This is my phone number:455-525-4523")
print(mo.group(1)) # first paranthesis
print(mo.group(2)) # second paranthesis
print(mo.group())  # complete string match
print(mo.group(0)) # Group 0 returns entire matched text.
print(mo.groups()) #Returns all groups at once in a tuple.
areaCode,mainNum = mo.groups()
print('Are code is:'+areaCode)
print('Main number is:'+mainNum)
