class car:
    def __init__(self,company,auto_trans):
        self.company = company
        self.auto_trans = auto_trans
    def autotrans(self):
        print("your car has "+self.company)
    def color(self):
        print("your car color is white")

mycar = car("swift","autotrans_yes")
mycar.autotrans()
