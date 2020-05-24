import ipaddress
#from netaddr import IPAddress

while True:
    try:
        option = int(input(
"""
Please select the option as per your requirement:

1. I have an Ip address and CIDR, I would like to know
   network,first ip, last ip and Broadcast ip.
2. I have an Ip address and netmask, I would like to know
   network,first ip, last ip abd Broadcast ip.
3. I have a network address with CIDR, I would like to know
   first ip,last ip and Broadcast ip.\n"""))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try agian...!")
        continue

while True:
    if option == 1:
        Ip_add= input("Please enter the Ip address and CIDR like Ip/CIDR:")
        try:
            ipaddress.ip_interface(Ip_add)
        except ValueError:
            print("Oops! That doesn't looks like valid format. Please enter valid ip/CIDR:")
            continue
        print(Ip_add)
        ip_cidr = ipaddress.ip_interface(Ip_add)
        network_add =ipaddress.ip_network(ip_cidr.network)
        first_ip = network_add[1]
        last_ip = network_add[-2]
        Bcast_ip = network_add[-1]
        num_hosts = network_add.num_addresses
        print("Your network address is: "+str(network_add)+"\nYour first ip is "+str(first_ip)+"\nYour last ip is:"+str(last_ip)+"\nYour Bcast ip is:"+str(Bcast_ip)+"\nNumber of hosts are:"+str(num_hosts))
        break
        #
        # elif option == 2:
        # while True:
        #     Ip_addr = input("Please enter the Ip address:")
        #     try:
        #         ipaddress.ip_address(Ip_addr)
        #     except ValueError:
        #         print("Oops! That was not a valid Ip. Try agian...!")
        #         continue
        #     subnetmask = input("Please enter the subnet mask:")
        #     try:
        #
        # cidr = IPAddress(subnetmask).netmask_bits()
        # Ip_add_cidr = str(Ip_addr)+"/"+str(cidr)
        # ip_cidr = ipaddress.ip_interface(Ip_add_cidr)
        # network_add =ipaddress.ip_network(ip_cidr.network)
        # first_ip = network_add[1]
        # last_ip = network_add[-2]
        # Bcast_ip = network_add[-1]
        # num_hosts = network_add.num_addresses
        # print("Your network address is: "+str(network_add)+"\nYour first ip is "+str(first_ip)+"\nYour last ip is:"+str(last_ip)+"\nYour Bcast ip is:"+str(Bcast_ip)+"\nNumber of hosts are:"+str(num_hosts))
        # break
