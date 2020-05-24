import threading
import time

def sleeper(n,name):
    print("Hi, I am {}. Going to sleep for "+str(n)+" seconds\n".format(name))
    time.sleep(n)
    print("{} has woken up\n".format(name))

t = threading.Thread(target = sleeper, name = "My _First_Thread",args = (5,"Thread1"))

t.start()

print("Main program")
print("Main program")
