import math

answer = eval(input('Enter a number: '))
# answer =  949348294692  
num = answer
is_prime = True

sqrt = math.isqrt(num)

if num % 2 == 0:
	is_prime = False
	
else:
	for n in range(2, sqrt):
		if num % n == 0:
			is_prime = False

message = 'The number ' + str(answer) + ' is '
if is_prime:
	print(message + 'prime')
else:
	print(message + 'not prime')