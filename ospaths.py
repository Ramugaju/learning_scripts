import os
print(os.path.join('users','lib','apps'))
print(os.getcwd())
os.chdir('/Users/ramugaju')
print(os.getcwd())
print(os.listdir('/Users/ramugaju'))
#os.makedirs('/Users/ramugaju/food/delecious/waffles')
print(os.path.abspath('./'))
print(os.path.abspath('./food'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))