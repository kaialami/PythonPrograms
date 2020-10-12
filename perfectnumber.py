def perfect(num = 0):
	divisors = set()

	if num == 0:
		return False

	for x in range(1, num):
		if num % x == 0:
			divisors.add(x)

	sums = 0
	while True:
		for n in divisors:
			sums += n
			if sums >= num:
				break
		break

	if sums == num:
		return True
	else:
		return False


