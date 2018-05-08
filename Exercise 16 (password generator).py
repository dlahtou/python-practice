import random
import string

passlength = int(input("What length password is desired?: "))
passuppercase = input("Use uppercase? (Y/N)): ")
passdigits = input("Use numbers? (Y/N): ")
passspecialchars = input("Use special characters? (Y/N): ")

def yesnotoboolean(yesno):
	if yesno == "y" or yesno == "Y":
		return True
	else: return False

def pw_generator(pwlength, UC, Dig, Specials):
	s = string.ascii_lowercase
	if yesnotoboolean(UC):
		s += string.ascii_uppercase
	if yesnotoboolean(Dig):
		s += string.digits
	if yesnotoboolean(Specials):
		s += string.punctuation
	return "".join(random.sample(s,pwlength))
	
print(pw_generator(passlength, passuppercase, passdigits, passspecialchars))