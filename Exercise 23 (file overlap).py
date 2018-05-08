primeset = set()
happyset = set()

def readlines(filename, targetset):
	with open(filename, 'r') as open_file:
		line = open_file.readline()
		while line:
			line = int(line.strip('\n'))
			targetset.add(line)
			line = open_file.readline()
			
readlines('primenumbers.txt', primeset)
readlines('happynumbers.txt', happyset)

print(list(primeset & happyset))


