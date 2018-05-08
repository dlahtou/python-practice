import random
import sys

a = random.randint(1,9)
b = 0

while 1:
	b = b + 1
	guess = int(input("Guess a number!"))
	if guess == a:
		print("Correct!")
		break
	if guess > a:
		print("Your guess was too high!")
	if guess < a:
		print("Your guess was too low!")

print("You took %d guesses to get it right!" % b)

