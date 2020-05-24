ip_address_file=open('Ipaddress_list.txt')
for ip in ip_address_file:
        HOST=ip.strip()
        print('Configuring '+HOST)
