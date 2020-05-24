import telnetlib
import sys
import time
import getpass

HOST="10.122.161.16"
USER=raw_input("Eneter the username to login:")
password=getpass.getpass()
wait=1

tn=telnetlib.Telnet(HOST,23)
tn.read_until("Username:")
tn.write(USER+"\n")
if password:
    tn.read_until("Password:")
    tn.write(password+"\n")
    tn.write("config terminal\n")
    for i in range(21,41):
        tn.write("ip access-list extended T"+str(i)+"\n")
        for j in range(1,225):
            tn.write("deny ip host 10.0.0."+str(i)+ " host 10.0.0."+str(j)+"\n")
            time.sleep(.5)
    #for n in range(1,225):
        
        #tn.write(b"vlan "+str(n)+"\n")
        #tn.write(b"name pyhtnon_script_vlan_"+str(n)+"\n")
 #       time.sleep(.5)
print (tn.read_all())

    
