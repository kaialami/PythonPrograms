def sum_of_evens(lst):
	sums = 0
	for x in lst:
		for y in x:
			if y % 2 == 0:
				sums = sums + y
	return sums
					
				
def sum_of_ebens(lst):
    return sum([y for x in lst for y in x if y % 2 == 0])            
    
print(sum_of_evens([
    [1, 2, 3],
    [2, 3, 1]
    ]))

print('\nList comprehension method: ')
print(sum_of_ebens([
    [1, 2, 3],
    [2, 3, 1]
    ]))