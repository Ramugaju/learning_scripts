import ipaddress

def valid_ip(address):
    try: 
        ipaddress.ip_address(address)
        return True
    except:
        return False

print (valid_ip('10.10.20.30'))
print (valid_ip('2001:DB8::1'))
print (valid_ip('gibberish'))
print (valid_ip('255.255.255.255'))
