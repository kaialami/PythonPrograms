
def factors(number):
    import primefunction
    power = 0
    result = []
    
    if primefunction.isPrime(number):
        result.append([number, 1])
        return result

    # loop up to half of number to find factors
    for i in range(2, number//2 + 1):
        # divide number by prime numbers in ascending order
        if primefunction.isPrime(i) == True:
            while number % i == 0:
                while number % i == 0:
                    number = number // i
                    power += 1
                result.append([i, power])
    
            power = 0
    
    return result


def factorsAll(number):
    import primefunction
    power = 0
    result = []

    for i in range(2, number + 1):       
        if primefunction.isPrime(i) == True:
            while number % i == 0:
                while number % i == 0:
                    number = number // i
                    power += 1
            result.append([i, power])
    
            power = 0
    
    return result





def lcm(num1 = 0, num2 = 0):
    
    if num1 < 0 or num2 < 0:
        return 'Positive numbers please'

    factors1 = factors(num1)
    factors2 = factors(num2)
    list1 = {}
    list2 = {}
    
    if num1 == 0 or num2 == 0:
        return 0


    for x in factors1:
        a, b = x
        list1[a] = b
        
    for y in factors2:
        c, d = y
        list2[c] = d
    
    num1base = []
    num2base = []
    num1exp = []
    num2exp = []


    for x in list1:
        num1base.append(x)
        num1exp.append(list1.get(x))
    for y in list2:
        num2base.append(y)
        num2exp.append(list2.get(y))

    exponents = []
    final = []

# if numbers are the same:
    if list1 == list2:
         return multplyFactorsSameNum(list1, list2)

# if nums have same bases:
    elif num1base == num2base:
        for a, b in zip(num1exp, num2exp):
            
            if a >= b:
                exponents.append(a)
            else:
                exponents.append(b)

        for x, y in zip(num1base, exponents):
            result = x ** y
            final.append(result)

        ret = 1
        for x in final:
            ret = ret*x
        return ret

# if nums do not have same bases:
    else:
        dic1 = {}
        dic2 = {}
        finalbase = []

        for x in factorsAll(num1):
            a, b = x
            dic1[a] = b
        for y in factorsAll(num2):
            c, d = y
            dic2[c] = d
       
        
        

        if len(dic1) > len(dic2):
            for x in dic1:
                finalbase.append(x)
                if x in dic2:
                    continue
                else:
                    dic2[x] = 0
                
            
        else:
            for x in dic2:
                finalbase.append(x)
                if x in dic1:
                    continue
                else:
                    dic1[x] = 0
                

        for x, y in zip(dic1, dic2):
            get1 = dic1.get(x)
            get2 = dic2.get(y)

            if get1 >= get2:
                exponents.append(get1)
            else:
                exponents.append(get2)

        for a, b in zip(finalbase, exponents):
            result = a ** b
            final.append(result)

        ret = 1
        for k in final:
            ret = ret * k
        return ret





    

    
    
def multplyFactorsSameNum(list1, list2):
    final1 = []
    final2 = []
    exponents = []

    for product in list1:
        exp = product**list1.get(product)
        final1.append(exp)
    
    result = 1
    for x in final1:
        result = result*x
    return result



# print(factorsAll(13))  
# print(factorsAll(19))

#print(lcm(5000, 12))
                

#print(factorsAll(120))
#print(factors(12))


