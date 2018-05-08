import json
from collections import Counter

def getbirthdays():
    with open('birthdays.json', 'r') as open_file:
        birthdaydict = json.load(open_file)
    return birthdaydict

allbirthdays = getbirthdays()
birthdayswithnamedmonths = {}
monthsbynumber = {'1': 'January',
                '2': 'February',
                '3': 'March',
                '4': 'April',
                '5': 'May',
                '6': 'June',
                '7': 'July',
                '8': 'August',
                '9': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December'}

def tomonthname(monthnumber):
    return monthsbynumber[monthnumber]

for personsname in allbirthdays:
    ## remove everything in date string after the first '/' to get month number
    allbirthdays[personsname] = allbirthdays[personsname].split('/')[0]

    ## convert number to month name
    birthdayswithnamedmonths[personsname] = tomonthname(allbirthdays[personsname])

monthcount = Counter(list(birthdayswithnamedmonths.values()))

print(monthcount)
print(monthcount["December"])
