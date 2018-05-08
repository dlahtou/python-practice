def fibonacci_generator(y = 4):
	a = [1,1]
	while len(a) < y:
		a.append(a[len(a)-2] + a[len(a)-1])
	return a

inputint = int(input("How long of a sequence would you like?: "))
print(fibonacci_generator(inputint))