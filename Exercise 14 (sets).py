def list_duperemover(a = []):
	b = set()
	for i in a:
		if i not in b:
			b.add(i)
	return list(b)
	
q = [5, 10, 10, 15, 20, 25]

print(list_duperemover(q))