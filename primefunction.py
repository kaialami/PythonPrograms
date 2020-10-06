

def isPrime(answer):
    import math

    is_prime = True
    num = answer
    sqrt = math.isqrt(num)
    
    if num <= 3:
        is_prime = True

    elif num % 2 == 0:
        is_prime = False
        

    else:
         for n in range(2, sqrt + 1):
             if n % 2 ==0:
                 continue
			

             elif num % n == 0:
                 is_prime = False
                 
                 break
             else:
                 is_prime = True
    
    if is_prime == False:
        return False
    else:
        return True
    



