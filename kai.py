import statistics

def findNumberOfEvens(k = 0, w = [], printme = False):
	ret = 'put a value for k and k must be greater than 0'
	if (k is None):
		return ret
	if (k <= 0):
		return ret 

	c = 0
	w.append(k)
	w = sorted(w)
	
	if (printme == True):
			print('List of Evens: ')
	for n in w:
		if (n%2 == 0):
			if (printme == True):
				print(n)
			c += 1
		else:
			continue
	return c




def findNumber(m, a = []):
	empty = 'Please enter a number followed by a list of numbers.'
	if (m is None or m < 0):
		return empty
	if (a is None or a == []):
		return empty

	lg = len(a)
	q = 0
	for r in a:
		if (m == a[q]):
			found = 'Your number, ' + str(m) + ', was found!' 
			pos1 = ' It is in the first position.'
			pos2 = ' Its position is ' + str(q + 1) + ' from the left.'
			pos3 = ' It is in the last position.'
			if (q == 0):
				return found + pos1
			elif (q > 0 and q < (lg - 1) ):
				return found + pos2
			else:
				return found + pos3
			break

		else:
			q += 1
			if (q == lg):
				fail = 'Sorry, your number, ' + str(m) + ', is not in this list... Try a different number.'
				return fail
				break




