def perfect_slow(num):
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


def perfect_fail(num):
    from pfact import factors
    if num == 0:
        return False

    numFactors = factors(num)
    factList = []
    for x, y in numFactors:
        while y > 0:
            factList.append(x)
            y = y - 1

    size = len(factList)
    factSet = {1}

    for n in factList:
        factSet.add(n)
    
    # count = 1
    # for n in range(size - 1):
    #     factSet.add(factList[n] * factList[count])
    #     count += 1
    
    factNum = size - 1
    limit = 2
    while factNum > 1:
        for a in factList[:limit]:
            index = factList.index(a)
            product = a
            for x in range(factNum-1):
                product = product * factList[index + x + 1]
            factSet.add(product)
        factNum -= 1
        limit += 1
    
    print(factList)
    print(factSet)

    thesum = 0
    for v in factSet:
        thesum = thesum + v
    return True if thesum == num else False
    
def perfect_comb(num):
    from pfact import factors
    from itertools import combinations
    
    numFactors = factors(num)
    factList = []
    for x, y in numFactors:
        while y > 0:
            factList.append(x)
            y -= 1
    
    size = len(factList) - 1
    factSet = {1}
    for n in factList:
        factSet.add(n)
    cSet = set()
    while size > 1:
        comb = combinations(factList, size)
        for i in list(comb):
            if i in cSet:
                continue
            cSet.add(i)
            prod = 1
            for j in i:
                prod = prod * j
            factSet.add(prod)
        size -= 1

    finalSum = 0
    for k in factSet:
        finalSum = finalSum + k
    return True if finalSum == num else False

def perfect(num):
    from pfact import factors

    numFactors = factors(num)
    factList = []
    for x, y in numFactors:
        while y > 0:
            factList.append(x)
            y -= 1
    
    factSet = {1}
    for n in factList:
        factSet.add(n)
    
    clone = factList
    dec = len(clone)
    while dec > 1:
        prod = 1
        for i in factList:
            index = factList.index(i)
            prod = i
            for j in range(dec):
                if not index == j:
                    prod = prod * factList[j]
                factSet.add(prod)
        clone.remove(clone[0])
        dec = len(clone)
    
    if num in factSet:
        factSet.remove(num)
    final_sum = 0
    for n in factSet:
        final_sum = final_sum + n

    return True if final_sum == num else False
    

n = 28
if perfect(n):
    print(n,'is a perfect number')
else:
    print(n,'is not a perfect number')