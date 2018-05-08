from random import randint

## Generate secret number, initialize guess and counter variables
secret_number = randint(0,100)
guess = -1
incorrect_counter = 0

while secret_number != guess:

	## Ask user for a number, cast to int
	guess = int(input("Guess a number from 0 to 100: "))
	
	## Provide feedback and increment guess counter if user is wrong
	if guess < secret_number:
		print("your guess is low")
		incorrect_counter += 1
	elif guess > secret_number:
		print("your guess is high")
		incorrect_counter += 1
	
	## Print message if user is correct, exit
	else:
		print("you guessed right!")
		print("you won!")
		exit()
	
	## Exit game after 10 incorrect guesses
	if incorrect_counter == 10:
		print("you lost!")
		exit()