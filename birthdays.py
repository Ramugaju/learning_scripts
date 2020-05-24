birthdays = {'Alice':'April 6','Bob':'Dec 12'}

while True:
    print('Enter the name:(Blank for quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(name+' birthday is '+birthdays[name])
    else:
        print('Enter the birthdate of '+name)
        bday = input()
        birthdays[name] = bday
        print('Database updated with below details:\n')
        print(name+': '+birthdays[name])
