import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

with open('birthdays.json', 'r') as open_file:
    birthdaydict = json.load(open_file)

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


listbirthdaymonths = []
## generate list of month names
for key in birthdaydict:
    listbirthdaymonths.append(tomonthname(str(int(birthdaydict[key].split('/')[0]))))

monthcount = Counter(listbirthdaymonths)

x = []
y = []
for key in monthcount:
    x.append(key)
    y.append(monthcount[key])

output_file('birthdaymonthhistogram.html')

p = figure(x_range = list(monthsbynumber.values()))
p.vbar(x=x, top=y, width=0.5)

show(p)