import re
regex = r'([a-zA-Z]+) \d+'

matches = re.finditer(regex, "June 24, Aug 13 May 18")

for match in matches:
    print(match.group(1))
