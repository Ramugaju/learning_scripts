import threading
import time

class MyThread(threading.Thread):
    def __init__(self,number,func,args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args =args
    def run(self):
        print("Thread {} has started\n".format(self.number))
        self.func(*self.args)
        print("Thread {} has finished\n".format(self.number))

def double(number,cycles):
    for i in range(cycles):
        number+=number
    print(number)

threads_list = []

for n in range(50):
    t = MyThread(number = n+1,func = double, args = (n,3))
    threads_list.append(t)
    t.start()

for t in threads_list:
    t.join()
