import json
continueworking = True

def getbirthdays():
    with open('birthdays.json', 'r') as open_file:
        birthdaydict = json.load(open_file)
    return birthdaydict

def printnames():
    print("Welcome to the birthday dictionary dictionary. We know the birthdays of:")
    for key in getbirthdays().keys():
	    print(key)

def addbirthday():
    name = input("Enter the person's name: ")
    birthday = input("Enter %s's birthday: " % name)
    birthdaydict = getbirthdays()
    birthdaydict[name] = birthday
    with open('birthdays.json','w') as open_file:
        json.dump(birthdaydict,open_file)

printnames()

while continueworking:
    if input("Would you like to (A)dd or (R)ead a birthday?").lower() == 'a':
        addbirthday()
    else:
        printnames()
        name = input("Whose birthday would you like to know? ")
        print("%s has a birthday on %s" % (name, getbirthdays()[name]))
    if input("Quit? (y/n)").lower() == 'y':
        continueworking = False