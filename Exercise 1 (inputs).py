name = input("What is your name? ")
age = input("What is your age? ")
age = int(age)

yearat100 = 2117 - age


output = "Your name is " + name + " and you will be 100 years old in the year " + str(yearat100)
print(output)
f = input("Print how many copies?")
f = int(f)

print(f*(output+"\n"))
g = input("end?")