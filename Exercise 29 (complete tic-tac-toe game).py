import os
import time
clear = lambda: os.system('cls')

game = [[0,0,0],
		[0,0,0],
		[0,0,0]]
		
## usermove is defined as a duple with the row/column of a space in the game array
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
	game[usermove[0]][usermove[1]] = playernumber
	print("Player %s space (%s,%s)" % (playernumber, usermove[0], usermove[1]))
	
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

## Check for winner of completed game
for number in range(0,3):
	## check column 0
	firstrownumber = game[0][number]
	if game[1][number] == firstrownumber and game[2][number] == firstrownumber:
		quit("Winner found! Player %s in column %s!" % (firstrownumber, number +1))
	
	## check row 0
	firstcolumnnumber = game[number][0]
	if game[number][1] == firstcolumnnumber and game[number][2] == firstcolumnnumber:
		quit("Winner found! Player %s in row %s!" % (firstcolumnnumber, number+1))

## check diagonals
middle = game[1][1]
if game[0][0] == middle and game[2][2] == middle:
	quit("Winner found in falling diagonal! Player %s!" % middle)
if game[2][0] == middle and game[0][2] == middle:
	quit("Winner found in rising diagonal! Player %s!" % middle)
	
quit("STALEMATE! No winner found!")
	
	
