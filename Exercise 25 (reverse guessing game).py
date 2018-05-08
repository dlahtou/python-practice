correctguess = False
lowerbound = 0
upperbound = 100
guess = 50
guesscounter = 1

while not correctguess:
	print("Is " + str(guess) + " your number?")
	if input("(y/n): ") == 'y':
		print("I got it correct after " + str(guesscounter) + " guesses!")
		break
	
	##ask for a hint
	if input("Was my guess too -low- or too -high-? ") == 'low':
		lowerbound = guess
	else:
		upperbound = guess
	
	guess = int((lowerbound + upperbound)/2)
	
	guesscounter += 1

