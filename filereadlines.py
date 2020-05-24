#fileopen=open('/Users/ramugaju/sonnet.txt')
#fileopen.readlines()
#print(fileopen)

baconFile=open('/Users/ramugaju/bacon.txt','w')
baconFile.write('Hello world!\n')

baconFile.close()
baconFile=open('/Users/ramugaju/bacon.txt','a')
baconFile.write('Bacon is not a vegetable\n')

baconFile.close()
baconFile=open('/Users/ramugaju/bacon.txt')
content=baconFile.read()
baconFile.close()
print(content)
