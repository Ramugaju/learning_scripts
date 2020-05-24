while True:
    Name = input("Enter your name:")
    if Name != "Joe":
       continue
    else:
       password = input("Enter your passowrd:")
    if password != "swordfish":
        print("Access Denied")
    else:
        print("Access Granted")
        break
    

