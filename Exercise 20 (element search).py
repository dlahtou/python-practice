a = [1, 3, 5, 30, 42, 43, 500]
aindex = 0

searchednumber = int(input("Enter a number: "))

while searchednumber != a[aindex]:
	aindex += 1
	if aindex == len(a):
		print("Number is not in the list!")
		break
	if searchednumber == a[aindex]:
		print("%d is in the list!" % searchednumber)
		break