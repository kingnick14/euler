import math
inp = int(input('Enter a number:'))
factors = []
mirrors = []
storeme = 0
fulllist = []
primes = []
#rangelist = list(range(0,inp))
def isprime(rangetop):
    holder = []
    del holder[:]
    print(rangetop)
    checker = range(1,int(math.sqrt(rangetop)+1))
    for a in checker:
        #print('debug',rangetop % a, ' is remainder of',a)
        if rangetop % a == 0:
            holder.append(a)
    if len(holder) == 1: return True


###### check for the square root, all facotrs have to be below or above this number
###### check every int below the square, and check for its mirror, if they are primes
###### create a function that does the above check, and call it whenever you get a factors
###### profit


### find SquareRoot of inp
rangelist = list(range(2,int(math.sqrt(inp)+1)))
print('#s below SquareRoot:',rangelist)
### search for factors up to SquareRoot of Inp
for i in rangelist:
    if not inp % i == 0: continue
    factors.append(i)
print('factors:',factors)

### find mirrors of factors
for x in factors:
    storeme = int(inp / x)
    mirrors.append(storeme)
print('mirrors:', mirrors)
### combine factors and mirrors
fulllist = factors + mirrors
print('Full list:',fulllist)

for z in fulllist:
    if isprime(z,z) == True:
        primes.append(z)
    #print('debug 2:', z)

primes.sort()
print('Your primes are', primes)
### Check for primes bz dividing and storing factors and looking for len of 2

# for y in fulllist:
#     print(y)
#     div = []
#     cand = []
#     div = list(range(1,y)
#     for z in div:
#         if z % y == 0
#             cand.append(z)
    #if len(cand) == 2: primes.append(y)

# nextf = int(inp) - 1
# while nextf > 1:
#     fulllist.append(nextf)
#     rem = int(inp) % nextf
#     if not rem == 0:
#         nextf = nextf - 1
#         continue
#     else:
#         for i in fulllist:
#             if  (nextf % i) == 0:
#                 lst.append(nextf)
#                 nextf = nextf - 1
#                 continue

#for factors in list:


#print(fulllist)
# newrange = []
# for i in rangelist[2:]:
#     rem = int(inp) % i
#     if not rem == 0:
#         continue
#     else:
#         del newrange[:]
#         newrange = list(range(2,i))
#         for x in newrange:
#
#             if  (i % x) != 0 and  x not in lst:
#                 lst.append(x)



#print (sum(lst))
#print(lst)
