import os
import time
clear = lambda: os.system('cls')

game = [[0,0,0],
		[0,0,0],
		[0,0,0]]
		
def getmove(playernumber):
	usermove = input("PLAYER %s: Pick a square (row,col): " % playernumber).strip().split(',')
	usermove = [int(i) for i in usermove]
	return usermove

def checkspace(usermove):
	if game[usermove[0]][usermove[1]] == 0:
		return True
	else:
		return False

def placecharacter(usermove,playernumber):
	character = 'X'
	if playernumber == 2:
		character = 'O'	
	game[usermove[0]][usermove[1]] = character
	print("Placed %s in space (%s,%s)" % (character, usermove[0], usermove[1]))
	
def printgame():
	print(game[0])
	print(game[1])
	print(game[2])
		
playerturn = 1
usermove = [0,0]

while 0 in game[0] or 0 in game[1] or 0 in game[2]:
	validmove = False
	printgame()
	
	## input player move while ensuring it is valid
	while not validmove:
		print("Please enter a valid move.")
		usermove = getmove(playerturn)
		validmove = checkspace(usermove)
	
	
	placecharacter(usermove,playerturn)
	time.sleep(2)
	
	## change turns
	if playerturn == 1:
		playerturn = 2
	else:
		playerturn = 1
	clear()

print("All spaces filled!")
printgame()
	
	

