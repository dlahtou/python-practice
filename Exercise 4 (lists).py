num = input("Input a number: ")
num = int(num)
x =[]

for elem in range(1,num):
	if num % elem == 0:
		x.append(elem)
	
print(x)
input("Press enter to end.")