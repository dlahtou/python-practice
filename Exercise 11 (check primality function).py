usrnumber = int(input("Type a number: "))

def is_divisible(input_number):
	i = 2
	p = 1
	while i*i <= input_number:
		if input_number % i == 0:
			return("%d is divisible by %d!" % (input_number, i))
			p = 0
		i = i + 1
	if p == 1:
		return("%d is prime!" % input_number)

print(is_divisible(usrnumber))