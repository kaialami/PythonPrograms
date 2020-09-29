

def find_prime(answer):
	import math

	is_prime = True
	even = False
	flt = isinstance(answer, float)
	fltans = answer

	if flt == True:
		up = False
		answer = int(answer)
		if fltans >= float(answer) + 0.5:
			answer = answer + 1
			up = True

	num = answer

	sqrt = math.isqrt(num)

	if num % 2 == 0:
		is_prime = False
		even = True

	else:
		for n in range(2, sqrt + 1):
			if n % 2 == 0:
				continue

			if num % n == 0:
				is_prime = False
				factor = n
				break

	strans = str(answer)
	message = 'The number ' + strans + ' is '
	rdup =  str(fltans) + ' was rounded up to ' + strans + '.'
	rddown = str(fltans) + ' was rounded down to ' + strans + '.'

	if flt == True:
		if up == True:
			if is_prime:
				return message + 'prime. ' + rdup

			else:
				if even == True:
					return message + 'not prime. ' + strans + ' is divisble by 2. ' + rdup
				else:
					return message + 'not prime. ' + strans + ' is divisble by ' + str(factor) + '. ' + rdup
		else:
			if is_prime:
				return message + 'prime. ' + rddown

			else:
				if even == True:
					return message + 'not prime. ' + strans + ' is divisble by 2. ' + rddown
				else:
					return message + 'not prime. ' + strans + ' is divisble by ' + str(factor) + '. ' + rddown

	else:
		if is_prime:
			return message + 'prime.'

		else:
			if even == True:
				return message + 'not prime. ' + strans + ' is divisble by 2.'
			else:
				return message + 'not prime. ' + strans + ' is divisble by ' + str(factor) + '.'

