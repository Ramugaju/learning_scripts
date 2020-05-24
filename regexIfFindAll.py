import re

regex = r'([a-zA-Z]+) \d+'

matches = re.findall(regex, "May 18 Dec 25 july 25")
print(matches)
for match in matches:
    
    print("full match: %s"%(match))


