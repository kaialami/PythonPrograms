from random import randint
from dicefunct import dice

while True:

	count = input('How many dice to roll?: ')

	while True:
		try:
			int(count)
			break
		except:
			count = input('Enter a number: ')

	count = int(count)
	if count <= 0:
		print('The number must be positive.')
		continue

	for x in range(count):
		r = randint(1, 6)
		dice(r)

	ask = input('Roll again? ([y] n): ').lower()
	while True:
		if ask == 'y' or ask == 'n':
			break
		else:
			ask = input('Enter y or n: ').lower()

	if ask == 'y':
		continue
	else:
		break



