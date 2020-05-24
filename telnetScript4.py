#!/usr/bin/env/ python

import telnetlib
import getpass
import sys
import time

user = raw_input("Enter the Username:")
password = getpass.getpass()
for n in range (41,45):
    print "Telnet to host" + str(n)
    HOST = "192.168.122." + str(n)
    print(HOST)
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write(user+"\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("conf t\n")
    tn.write("int vlan 1\n")
    tn.write("ip address 10.1.1."+str(n)+"\n")
    tn.write("exit\n")
    tn.write("router ospf 1\n")
    tn.write("network 10.1.1.0 0.0.0.255 area 0\n")
    tn.write("end\n")
    tn.write("wr\n")
    time.sleep(1)
    tn.write("exit\n")
    print tn.read_all()
