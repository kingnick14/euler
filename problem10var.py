import primefinder
import math
import time
inp  = input('Enter a number:')
start = time.time()
sumtotal = 0
for i in range(1,int(inp)+1):
    if primefinder.isprime(i) == True:
        sumtotal += i

print(sumtotal)
print('Elapsed time:', time.time() - start)
