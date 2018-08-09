import primefinder
import math
import time


inp  = input('Enter a number:')
start = time.time()
storeme = []
for i in range(1,int(inp)+1):
    if primefinder.isprime(i) == True:
        storeme.append(i)
#print(storeme)
print(sum(storeme))

print('Elapsed time:', time.time() - start)
