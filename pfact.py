
def factors(number):
    import prime
    power = 0
    result = []
    
    if prime.isPrime(number):
        result.append([number, 1])
        return result

    for i in range(2, number//2 + 1):
        if prime.isPrime(i) == True:
            while number % i == 0:
                while number % i == 0:
                    number = number // i
                    power += 1
                result.append([i, power])
    
            power = 0
    
    return result


def factorsAll(number):
    import prime
    power = 0
    result = []

    for i in range(2, number + 1):       
        if prime.isPrime(i) == True:
            while number % i == 0:
                while number % i == 0:
                    number = number // i
                    power += 1
            result.append([i, power])
    
            power = 0
    
    return result


def lcm(num1 = 0, num2 = 0):

    if not isinstance(num1, int) or not isinstance(num2, int):
        return 'Positive whole numbers please'

    elif num1 < 0 or num2 < 0:
        return 'Positive numbers please'

    elif num1 == 0 or num2 == 0:
        return 0

    elif num1 == num2:
        return num1

    factors1 = factorsAll(num1)
    factors2 = factorsAll(num2)
    dict1 = {}
    dict2 = {}
    num1base = []
    num2base = []
    exponents = []
    final = []

    for x in factors1:
        a, b = x
        dict1[a] = b
        num1base.append(a)

    for x in factors2:
        a, b = x
        dict2[a] = b
        num2base.append(a)

    if len(dict1) > len(dict2):
        finalbase = num1base
        for y in dict1:
            if y in dict2:
                continue
            else:
                dict2[y] = 0

    else:
        finalbase = num2base
        for y in dict2:
            if y in dict1:
                continue
            else:
                dict1[y] = 0

    for x, y in zip(dict1, dict2):
        get1 = dict1.get(x)
        get2 = dict2.get(y)

        if get1 >= get2:
            exponents.append(get1)
        else:
            exponents.append(get2)

    for a, b in zip(finalbase, exponents):
        result = a ** b
        final.append(result)

    ret = 1
    for n in final:
        ret = ret * n
    return ret


def gcf(num1 = 0, num2 = 0):

    if not isinstance(num1, int) or not isinstance(num2, int):
        return 'Positive whole numbers please'

    elif num1 < 0 or num2 < 0:
        return 'Positive numbers please'

    elif num1 == 0 or num2 == 0:
        return 0

    elif num1 == num2:
        return num1

    factors1 = factorsAll(num1)
    factors2 = factorsAll(num2)
    dict1 = {}
    dict2 = {}
    num1base = []
    num2base = []
    exponents = []
    final = []

    for x in factors1:
        a, b = x
        dict1[a] = b
        num1base.append(a)

    for x in factors2:
        a, b = x
        dict2[a] = b
        num2base.append(a)

    if len(dict1) > len(dict2):
        finalbase = num1base
        for y in dict1:
            if y in dict2:
                continue
            else:
                dict2[y] = 0

    else:
        finalbase = num2base
        for y in dict2:
            if y in dict1:
                continue
            else:
                dict1[y] = 0

    for x, y in zip(dict1, dict2):
        get1 = dict1.get(x)
        get2 = dict2.get(y)

        if get1 >= get2:
            exponents.append(get2)
        else:
            exponents.append(get1)

    for a, b in zip(finalbase, exponents):
        result = a ** b
        final.append(result)

    ret = 1
    for n in final:
        ret = ret * n
    return ret



 # FIRST ATTEMPT AT LCM/GCF (bad, kept for reference.)
# def lcm(num1 = 0, num2 = 0):
    
#     if num1 < 0 or num2 < 0:
#         return 'Positive numbers please'

#     factors1 = factors(num1)
#     factors2 = factors(num2)
#     list1 = {}
#     list2 = {}
    
#     if num1 == 0 or num2 == 0:
#         return 0


#     for x in factors1:
#         a, b = x
#         list1[a] = b
        
#     for y in factors2:
#         c, d = y
#         list2[c] = d
    
#     num1base = []
#     num2base = []
#     num1exp = []
#     num2exp = []


#     for x in list1:
#         num1base.append(x)
#         num1exp.append(list1.get(x))
#     for y in list2:
#         num2base.append(y)
#         num2exp.append(list2.get(y))

#     exponents = []
#     final = []

# # if numbers are the same:
#     if num1 == num2:
#         return num1

# # if nums have same bases:
#     elif num1base == num2base:
#         for a, b in zip(num1exp, num2exp):
            
#             if a >= b:
#                 exponents.append(a)
#             else:
#                 exponents.append(b)

#         for x, y in zip(num1base, exponents):
#             result = x ** y
#             final.append(result)

#         ret = 1
#         for x in final:
#             ret = ret*x
#         return ret

# # if nums do not have same bases:
#     else:
#         dic1 = {}
#         dic2 = {}
#         finalbase = []

#         for x in factorsAll(num1):
#             a, b = x
#             dic1[a] = b
#         for y in factorsAll(num2):
#             c, d = y
#             dic2[c] = d
       
        
        

#         if len(dic1) > len(dic2):
#             for x in dic1:
#                 finalbase.append(x)
#                 if x in dic2:
#                     continue
#                 else:
#                     dic2[x] = 0
                
            
#         else:
#             for x in dic2:
#                 finalbase.append(x)
#                 if x in dic1:
#                     continue
#                 else:
#                     dic1[x] = 0
                

#         for x, y in zip(dic1, dic2):
#             get1 = dic1.get(x)
#             get2 = dic2.get(y)

#             if get1 >= get2:
#                 exponents.append(get1)
#             else:
#                 exponents.append(get2)

#         for a, b in zip(finalbase, exponents):
#             result = a ** b
#             final.append(result)

#         ret = 1
#         for k in final:
#             ret = ret * k
#         return ret



# n1 = 2828
# n2 = 1


# print(lcm(n1, n2))
# print(gcf(n1, n2))

    



