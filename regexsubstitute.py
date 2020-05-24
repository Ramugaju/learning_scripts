import re
obj = re.compile(r'Agent \w+')
mo = obj.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob')
print(mo)

obj2 = re.compile(r'Agent (\w)\w*')
mo2 = obj2.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob')
print(mo2)
