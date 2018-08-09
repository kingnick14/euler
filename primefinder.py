import math

def isprime(n):
    if n == 1: return False
    elif n < 4: return True
    elif n % 2 == 0: return False
    elif n < 9: return True
    elif n % 3 == 0: return False
    else:
        rt = int(math.sqrt(n))
        i = 5
        while i <= rt:
            if n % i == 0:
                return False
                break
            if n % (i+2) == 0:
                return False
                break
            i += 6
        return True
