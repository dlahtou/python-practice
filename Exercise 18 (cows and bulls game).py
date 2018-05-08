import random

def cowchecker(guess, actual):
	cows = 0
	for i in range(len(actual)):
		if guess[i] == actual[i]:
			cows = cows + 1
	return cows
	
def fourdigitmaker(numberstring):
	placeholder = numberstring
	while len(placeholder) < 4:
		placeholder = "0" + placeholder
	return placeholder

if __name__=="__main__":
	secretnumber = fourdigitmaker(str(random.randint(0,9999)))
	playing = True
	guessed = 0

	while playing:
		userguess = input("Enter a number: ")
		cleanuserguess = fourdigitmaker(userguess)
		guessed += 1
		yourcows = cowchecker(cleanuserguess, secretnumber)
		if yourcows == 4:
			print("%s is the secret number!" % userguess)
			print("It took you %d guesses!" % guessed)
			playing = False
		else:
			print("You have %d cows and %d bulls" % (yourcows, 4-yourcows))