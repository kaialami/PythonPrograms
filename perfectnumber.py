def perfect1(num):
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

def perfect(num):
    from pfact import factors
    
    if num == 0:
        return False
    
    numFactors = factors(num)
    
         factList = []
    
         for x, y in numFactors:
                 while y > 0:
                         factList.append(x)
                         y = y -1

         size = len(factList)
    
         factSet = {1}

         for n in factList:

                 factSet.add(n)

         np = len(factList)
    while np >= 0:
        for n in factList:
    
                         index = factList.index(n)
    
                         for x in range(size - 1):
                
                                 if not x == index:
                    
                                                              factSet.add(n * factList[x])
        np = np - 1
    
    print(numFactors)
    print(factList)
    print(factSet)
    

perfect(100)
