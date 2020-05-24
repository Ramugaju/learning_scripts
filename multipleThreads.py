import threading
import time

def sleeper(n,name):
    print("Hi, I am {}. Going to sleep for ".format(name)+str(n)+" seconds\n")
    
    time.sleep(n)
    print("{} has woken up\n".format(name))

threads_List = []

start = time.time()

for i in range(5):
    t = threading.Thread(target = sleeper, name = "Thread{}".format(i), args = (5,"Thread{}".format(i)))
    threads_List.append(t)
    t.start()
    print("Thread{} has started".format(i))

for t in threads_List:
    t.join()
end = time.time()
print("Time take:{}".format(end-start))
print("All five threads have finished")
