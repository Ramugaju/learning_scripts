def split(ip):
    splitList = ip.split(".")
    #print(splitList)
    for i in range(len(splitList)):
        if int(splitList[i]) > 255:
            #print(ip+" is invalid")
            return False
            break
        else:
            continue
    return True

ip = "192.168.1.0"
if split(ip):
    print (ip+" is valid")
else:
    print (ip+" is invalid")
