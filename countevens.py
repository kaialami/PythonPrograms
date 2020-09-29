answer = eval(input('Enter a number: '))
rest = answer
count = 0

while (rest > 0):
	rightdigit = rest % 10
	rest = rest // 10
	if (rightdigit % 2 == 0):
		count += 1

print('The number of even digits in ', answer, ' is ',count)
