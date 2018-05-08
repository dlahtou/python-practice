a = [5, 10, 15, 20, 25]
b = []

def list_ends(z):
	y = []
	y.append(z[0])
	y.append(z[len(z)-1])
	return y

print(list_ends(a))