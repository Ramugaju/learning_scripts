import re
import ipaddress

f = open('/Users/ramugaju/documents/regexfile.txt')

#f.write("When, in disgrace with fort june 24 une and men's eyes,\nI all alom may 18 ne beweep my outcast state,\ntrouble deaf heav Aug 15 en with my bootless cries,\nAnd look upon myself and curse my fate")

#f.write("Hello world")


#content = f.readlines()

#for i in content:

#    k = i.strip()
    
#    print(k)

def valid_ip(address):
    try: 
        ipaddress.ip_address(address)
        return True
    except:
        return False

"""

"""
for line in f:
    
    if re.search("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",line):
        
       match = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",line)

       print(match)

       for i in range(len(match)):
           print(match[i])
           if valid_ip(match[i]):
               print(match[i]+" is valid ip")

               regexipFile = open("/users/ramugaju/documents/regexFileIp.txt",'a')
               regexipFile.write(match[i]+"\n")
               regexipFile.close()

f.close()
