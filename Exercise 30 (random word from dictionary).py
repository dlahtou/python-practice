import random

sowpodswordlist = []
printword = True

with open('sowpods.txt','r') as open_file:
	sowpodswordlist = open_file.readlines()

sowpodswordlist = [i.strip('\n') for i in sowpodswordlist]

while printword:
	print(random.choice(sowpodswordlist))
	if input("Want another word? (y/n)").lower() == 'n':
		printword = False