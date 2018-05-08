namedictionary = {}

with open('nameslist.txt', 'r') as open_file:
	line = open_file.readline()
	while line:
		line = line.strip('\n')
		if line in namedictionary:
			namedictionary[line] += 1
		else:
			namedictionary[line] = 1
		line = open_file.readline()
	for key in namedictionary:
		print(key + ": " + str(namedictionary[key]))