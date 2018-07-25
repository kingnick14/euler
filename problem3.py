inp = int(input('Enter a number:'))
fulllist = []
lst = []
#rangelist = list(range(0,inp))


###### check for the square root, all facotrs have to be below or above this number
###### check every int below the square, and check for its mirror, if they are primes
###### create a function that does the above check, and call it whenever you get a factors
###### profit

nextf = int(inp) - 1
while nextf > 1:
    fulllist.append(nextf)
    rem = int(inp) % nextf
    if not rem == 0:
        nextf = nextf - 1
        continue
    else:
        for i in fulllist:
            if  (nextf % i) == 0:
                lst.append(nextf)
                nextf = nextf - 1
                continue

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



print (sum(lst))
print(lst)
