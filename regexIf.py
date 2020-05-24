import re

regex = r'([a-zA-Z]+) (\d+)'

if re.search(regex, "may 18"):
    match = re.search(regex, "may 18")
    print("Match at Index %s, %s" %(match.start(),match.end()))

    print("Full match: %s" %(match.group()))
    print("Month: %s" %(match.group(1)))
    print("Day: %s" %(match.group(2)))
          
else:
    print("Not Found")
