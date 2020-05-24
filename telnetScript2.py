#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()


for n in range (41,45):
    print "Telnet to host" + str(n)
    HOST = "192.168.122." + str(n)
    print(HOST)
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
       tn.read_until("Password: ")
       tn.write(password + "\n")

    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("conf t\n")
    tn.write("no int loop 0\n")
   # tn.write("ip address 1.1.1.1 255.255.255.255\n")
    tn.write("no int loop 1\n")
   # tn.write("ip address 2.2.2.2 255.255.255.255\n")
    tn.write("no router ospf 1\n")
   # tn.write("network 0.0.0.0 255.255.255.255 area 0\n")
    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()
