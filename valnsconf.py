import telnetlib
import sys
import time
import getpass

HOST="10.122.161.16"
USER=input("Eneter the username to login:")
password=getpass.getpass()
wait=1

tn=telnetlib.Telnet(HOST,23)
tn.read_until(b"Username:")
tn.write(USER.encode('ascii')+b"\n")
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"config terminal\n")
    tn.write(b"ip access-list extended TEST"+"\n")
    for n in range(2,225):
        tn.write(b"permit ip host 10.0.0.1 host 10.0.0."+str(n)+"\n")
        #tn.write(b"vlan "+str(n)+"\n")
        #tn.write(b"name pyhtnon_script_vlan_"+str(n)+"\n")
        time.sleep(.5)
print (tn.read_all())
    
