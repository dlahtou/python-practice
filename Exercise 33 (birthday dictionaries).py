birthdaydict = {"Daniel": "12/7/90",
				"Noob": "1/1/1901",
				"Will": "3/24/1995"}

print("Welcome to the birthday dictionary dictionary. We know the birthdays of:")
for key in birthdaydict.keys():
	print(key)

name = input("Whose birthday would you like to know? ")
print("%s has a birthday on %s" % (name, birthdaydict[name]))