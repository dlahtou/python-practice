number = input("Input a number: ")
number = int(number)

check = input("Input a quotient: ")
check = int(check)

if number % 4 == 0:
	print(str(number) + " is a multiple of 4!")
elif number % 2 == 0:
	print(str(number) + " is an even number!")
else:
	print(str(number) + " is an odd number!")
	
if number % check == 0:
	print(str(number) + " is divisible by " + str(check) + "!")

input("Press enter to end.")