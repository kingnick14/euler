import time
import math
def isprime(no):
    holder = []
    del holder[:]
    #print(no)
    checker = range(1,int(math.sqrt(no)+1))
    for a in checker:
        #print('debug',rangetop % a, ' is remainder of',a)
        if no % a == 0:
            holder.append(a)
    if len(holder) == 1: return True

inp = input('What nth prime would you like to find?')
try:
    inp = int(inp) + 1
except:
    print('Please enter an integer!')
    exit()
start = time.time()
ran = range(3,inp)
primes = []
numbers = 2
while True:
    if len(primes) == inp - 1:
        print(max(primes))
        print('Elapsed time:', time.time() - start)
        break
    if isprime(numbers) == True:
        primes.append(numbers)
    numbers += 1
