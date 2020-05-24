class MyClass:
    variable = 'blah'
    def function(self):
        print('This is a message inside the class')
myObjectx = MyClass()
myObjecty = MyClass()

myObjectx.variable = 'yackity'

print(myObjectx.variable)
print(myObjecty.variable)

myObjectx.function()
