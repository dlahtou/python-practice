secretword = 'EVAPORATE'
guessedletters = set()
guessed = False

def showhangman():
	hangmanstring = ""
	for letter in secretword:
		if letter.lower() in guessedletters:
			hangmanstring += letter.upper() + " "
		else:
			hangmanstring += "_ "
	print(hangmanstring)

def checkletter(letter):
	if letter.upper() in secretword:
		return True
	else:
		return False
	
def checkhangmancomplete():
	for letter in secretword:
		if letter.lower() not in guessedletters:
			return False
	print("You guessed the whole word! Well done!")
	return True

print("Welcome to Hangman!")

while not guessed:
	showhangman()
	newletter = input("Guess your letter: ").lower()
	guessedletters.add(newletter)
	
	if checkletter(newletter):
		print("%s is in the word!\n" % newletter.upper())
	else:
		print("%s is not in the word! Guess again!\n" % newletter.upper())
	guessed = checkhangmancomplete()