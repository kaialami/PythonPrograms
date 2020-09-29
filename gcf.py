# answer = eval(input('Enter a number: '))
answer1 = 21
answer2 = 25
num1 = answer1
num2 = answer2

# finding factors of answer1
if num1 % 2 == 0:
	while num1 % 2 == 0:
		num1 = num1 // 2
		print(num1)

else:
	for n in range(2, num1):
		if n % 2 == 1:
			print(n)



