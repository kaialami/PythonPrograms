def fib(n):
	if n<0:
		return -1
	if n<1:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

def fibSearch(lst, x):
	size = len(lst) # Size of the list

    # Fibonacci index
	m = 0
    

    #Find the smallest fibonacci index that is 
    #greater or equal to the size of the list
	while fib(m) < size:  
		m = m + 1 

	# the variable offset is a bookmark to indicate 
	# the index of the lower bound of the search region.
	# it is set to -1, because the list indexing in Python
	# starts at 0.  so the first lower bound (which is fib(m-2)) 
	# should be adjusted by -1 to get the correct ordinal for the list item.
	offset = -1   

	while (fib(m) > 1):
		print("Upper bound m =", fib(m), ", m-1 =", fib(m-1), ", Lower bound m-2 =", fib(m-2))
		print("lower bound will be adjusted by: ", offset)

    	# Find the lower bound of the search region
    	# if we are at the start of the search, offset is -1 to give us the 
    	# correct item in the list for the lower bound.  otherwise,
    	# the new lower bound for search region is new lower bound adjusted by
    	# the previous lower bound (offset).
		lstIndex = min( offset + fib(m - 2) , len(lst) - 1)

		print("the lower bound is now at index: ", lstIndex)
		print('\nelement at index [',lstIndex,"] is:",lst[lstIndex])
        
        #if the searched item is greater than the list item at index
        #then move the upper bound of the search by 1 fibonacci number
        #and set the current index to be the offset from the lower bound of the new
        #search region
		if (x > lst[lstIndex]):  
			m = m - 1
			offset = lstIndex
			print('the desired value (',x,') is greater than the lower bound.  \nthe offset(= ',offset,') is placed at the lower bound as a bookmark.')
			print('the region is shifted down by one fibonacci number.\n')

        # else if the searched item is smaller than the list item at the current index
        # that means the desired number is not in the search region and we can modify the
        # upper bound to move by 2 fibonacci numbers
		elif (x < lst[lstIndex]):
			m = m - 2
			print('the desired value (',x,') is not in the region.  the region is shifted by two fibonacci numbers.')
        
        # otherwise, the list item at the current index must be the desired number
        # so we return the current index
		else:
			print('the desired value is at the lower bound.')
			return lstIndex

	if(fib(m - 1) != -1 and lst[offset + 1] == x):
		print('i am here')
		return offset + 1
	return -1

lst = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130] 
x = 60    
print(lst)
print('Number found at index : ',fibSearch(lst, x))		