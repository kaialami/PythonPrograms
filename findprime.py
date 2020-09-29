# answer = eval(input('Enter a number'))
answer = 7523177777
number = answer
isPrime = True

for count in range(2, number):
	if (number % count) == 0:
		isPrime = False
		break
if isPrime:	
	print('After ', count - 1, ' iterations, we found that the number is prime')
else:
	print('After ', count - 1, ' iterations, we found that it is not a prime number')


11