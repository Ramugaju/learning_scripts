class vehicle:
    name=""
    kind="Car"
    color=""
    value=100.00
    def desc(self):
        desc_str="%s is a %s %s worth $%.2f." %(self.name,self.color,self.kind,self.value)
        return desc_str
car1=vehicle()
car2=vehicle()
print(car1.desc())
print(car2.desc())
