#!/usr/bin/env/ python

import telnetlib
import getpass
import sys
import time

user = raw_input("Enter the Username:")
password = getpass.getpass()

def telnet_ipadd(ip):
   print(ip)
   tn = telnetlib.Telnet(ip)
   tn.read_until("Username: ")
   tn.write(user+"\n")
   print("telnet done")

   if password:
        tn.read_until("Password: ")
        tn.write(password+"\n")
   print("connection estableshed to "+ip)


   tn.write("enable\n")
   tn.write("cisco\n")
   tn.write("conf t\n")
   tn.write("int loop 0\n")
   #tn.write("ip address 1.1.1.1 255.255.255.255\n")
   tn.write("int loop 1\n")
  # tn.write("ip address 2.2.2.2 255.255.255.255\n")
#   tn.write("router ospf 1\n")
 #  tn.write("network 0.0.0.0 255.255.255.255 area 0\n")
   tn.write("end\n")
   tn.write("exit\n")

   print tn.read_all()
for n in range (41,45):
    print "Telnet to host" + str(n)
    HOST = "192.168.122." + str(n)
    print(HOST)
    telnet_ipadd(HOST)
#f = open("ip-address-file.txt")

#for i in f:
 #   HOST = i.strip()
  #  print("Configuring: "+HOST)
   # telnet_host(HOST)
