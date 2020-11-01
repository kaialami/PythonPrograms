def isMember(num, lst):
    for i in lst:
        if i == num:
            return True
    return False

def binaryMember(num, lst):
    clone = lst[:]
    size = len(clone)
    pivot = size // 2
    while pivot >= 1: 
        pivot = size // 2
        if clone == []:
            return False
        elif num == clone[pivot]:
            print(clone, size, pivot)
            return True
        elif num < clone[pivot]:
            clone = clone[:pivot]
            size = len(clone)
            print(clone, size, pivot)
        else:
            clone = clone[pivot + 1:]
            size = len(clone)
            print(clone, size, pivot)
    return False
    
def fibMember1(num, lst):
    clone = lst.copy()
    size = len(clone)
    fib = {0:0, 1:1}
    for n in range(2, size + 5):
        fib[n] = fib.get(n-2) + fib.get(n-1)
    print(fib)
    dec = len(fib) - 1
    while size <= fib.get(dec):
        dec -= 1
    fibM = fib.get(dec + 1)
    m = dec + 1
    mth = m + 1

    # while size > 0:
    #     m1 = m - 1
    #     m2 = m -2
    #     if num == fibM2:
    #         return True

def fibMember(num, lst):
    size = len(lst)
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1
    while fib < size:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    off = -1
    while fib > 1:
        i = min(fib2 + off, size-1)
        if num == lst[i]:
            return True
        elif num < lst[i]:
            fib = fib2
            fib1 = fib1 - fib
            fib2 = fib - fib1
        else:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            off = i
    return False


from random import randint
number = -111
lst = []
for x in range(10):
    lst.append(randint(1, 10))
sortedLst = sorted(lst)
print(sortedLst)
print(fibMember(number, sortedLst))