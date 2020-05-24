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
    tn.write("username ramu password cisco\n")
    tn.write("end\n")
    tn.write("exit\n")
    print tn.read_all()
