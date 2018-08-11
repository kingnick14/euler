import time
import math

count = 0
start = time.time()
trino= 0
holder = []
while True:
    holder = []
    trino = trino + count
    count += 1
    for a in range(1,int(math.sqrt(trino))):
        #print('debug',trino % a, ' is remainder of',a)
        if trino % a == 0:
            holder.append(a)
    if len(holder) >= 250: break
print (trino)
print(count-1)
print(len(holder))
print('Elapsed time:', time.time() - start)
