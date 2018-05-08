import random
import os
import time
clear = lambda: os.system('cls')

sowpodswordlist = []

with open('sowpods.txt','r') as open_file:
	sowpodswordlist = open_file.readlines()

sowpodswordlist = [i.strip('\n') for i in sowpodswordlist]
playagain = True
gamecounter = 0
wincounter = 0

def playgame():
	secretword = random.choice(sowpodswordlist)
	guessedletters = set()
	guessed = False
	guesscounter = 0

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

	def alreadyguessed(letter):
		if letter in guessedletters:
			return True
		return False
		
	def checkhangmancomplete():
		for letter in secretword:
			if letter.lower() not in guessedletters:
				return False
		print("You guessed the whole word! Well done!")
		print(secretword)
		return True


	print("Welcome to Hangman!")

	while not guessed and guesscounter < 6:
		clear()
		showhangman()
		print("You have %s wrong guesses left!" % (6-guesscounter))
		newletter = input("Guess your letter: ").lower()
		if alreadyguessed(newletter):
			print("You already guessed %s! Try again!" % newletter.upper())
			time.sleep(3)
			continue
		guessedletters.add(newletter)
		
		if checkletter(newletter):
			print("%s is in the word!\n" % newletter.upper())
			time.sleep(3)
		else:
			print("%s is not in the word!" % newletter.upper())
			guesscounter += 1
			if guesscounter == 6:
				print("You lose! The word was %s" % secretword)
				return False
			print("Guess again!")
			time.sleep(3)
		if checkhangmancomplete():
			return True

while playagain:
	if playgame():
		wincounter += 1
	gamecounter += 1
	print("You've played %s games with %s wins!" % (gamecounter, wincounter))
	if input("Would you like to play again (y/n)?").lower() == 'n':
		playagain = False