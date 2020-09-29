answer = eval(input('Enter a number: '))
rest = answer
total = 0

while (rest > 0):
	rightdigit = rest % 10
	rest = rest // 10
	total = total + rightdigit

print('sum of all digits in ', answer,' is ',total)
