possidrome = str(input("Input a word: "))
reverseword = possidrome[::-1]

if possidrome == reverseword:
	print("Palindrome!")
else:
	print("Not a palindrome!")