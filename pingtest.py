import ipaddress
import subprocess
from subprocess import Popen, PIPE
import time

ip_net = ipaddress.ip_network('192.168.0.100/30')
for i in ip_net.hosts():
    # print(i)
    host_add = str(i)
    toping = subprocess.Popen(['ping', '-n', '3',host_add],stdout=PIPE)

    output = toping.communicate()[0]
    hostalive = toping.returncode
    if hostalive == 0:
        print(host_add,"is reachable")
    else:
        print(host_add,"is not reachable")
    # print(output)
    # time.sleep(3)
    # if toping ==0:
    #     print(i, ' is alive')
    # else:
    #     print(i,' is not alive')
