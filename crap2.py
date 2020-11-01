def fibMember(num, lst):
    # clone = lst.copy()
    clone = lst
    size = len(clone)
    print(type(clone))
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
        print(i)
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

#print(fibMember(57888,list(range(1,2**20))))
print(fibMember(98763,range(1,2**60)))
#print(2**20)
