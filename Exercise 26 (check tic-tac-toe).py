game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

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