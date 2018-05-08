def linebuilder(size):
	horizontal = ""
	vertical = ""
	for number in range(0,size+1):
		vertical += "|   "
		if number == 0:
			continue
		horizontal += " ---"
	return {'horizontal':horizontal, 'vertical':vertical}

size = int(input("How large of a tic-tac-toe board would you like? "))
constructionstrings = linebuilder(size)


## range does not include upper bound number
for number in range(0,size+1):
	print(constructionstrings['horizontal'])
	if number == size:
		break
	print(constructionstrings['vertical'])