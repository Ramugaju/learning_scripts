import os
totalsize=0
for filename in os.listdir('/Users/ramugaju'):
  totalsize=totalsize+os.path.getsize(os.path.join('/Users/ramugaju',filename))
print(totalsize)
