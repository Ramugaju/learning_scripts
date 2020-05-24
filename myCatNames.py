catNames = []
while True:
    print('Enter the name of Cat '+str(len(catNames)+1)+' (or nothing to stop)')
    name = input()
    if name == '':
        break
    catNames = catNames+[name]
print('My Cat names are:')
for i in catNames:
    print(i)
