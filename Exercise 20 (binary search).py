def binarysearch(orderedlist, guessnumber):
	upperend = len(orderedlist) -1
	lowerend = 0
	middle = int((upperend - lowerend)/2) #truncates decimals (floors result)
	while orderedlist[middle] != guessnumber:
		if orderedlist[upperend] < guessnumber or orderedlist[lowerend] > guessnumber:
			return("Your number is not in the list!")
		if orderedlist[middle] > guessnumber:
			upperend = middle
		if orderedlist[middle] < guessnumber:
			lowerend = middle
		print([lowerend, middle, upperend])
		middle = int((upperend-lowerend)/2)
	

if __name__== "__main__":
	a = [1, 3, 5, 30, 42, 43, 500]
	searchednumber = int(input("Enter a number: "))
	print(binarysearch(a, searchednumber))


	

