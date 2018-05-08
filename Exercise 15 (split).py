def stringreverser(fullstring = ""):
	spacedividedlist = fullstring.split(" ")
	reverselist = spacedividedlist[::-1]
	return " ".join(reverselist)

print(stringreverser("I have a chair"))