import random

while True:
	size = input('What size dice to roll? (6, 10, etc.): ')
	while True:
		try:
			int(size)
			break
		except:
			size = input('Please enter a number: ')

	size = int(size)
	
	if size <= 0:
		print('The number must be greater than 0')
		continue

	inp = input('How many dice to roll?: ')
	result = []

	while True:
		try:
			int(inp)
			break
		except:
			inp = input('Please enter a number: ')

	inp = int(inp)

	if inp <= 0:
		print('The number must be greater than 0')
		continue

	for x in range(inp):
		r = random.randint(1, size)
		result.append(r)

	print('Result: ' + str(result))

	ask = str(input('Roll again? ([y] n): '))

	while True:
		if ask == 'y' or ask == 'n':
			break
		else:
			ask = str(input('Enter y or n. ([y] n): '))

	if ask == 'y':
		continue
	else:
		break

