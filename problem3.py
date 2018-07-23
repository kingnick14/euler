inp = int(input('Enter a number:'))

lst = []
rangelist = list(range(0,inp))
nextf = int(inp) - 1
# while nextf > 1:
#     fulllist.append(nextf)
#     rem = int(inp) % nextf
#     if not rem == 0:
#         nextf -= 1
#         continue
#     else:
#         if nextf %
#         lst.append(nextf)
#         nextf -= 1

#for factors in list:


#print(fulllist)
newrange = []
for i in rangelist[2:]:
    rem = int(inp) % i
    if not rem == 0:
        continue
    else:
        del newrange[:]
        newrange = list(range(2,i))
        for x in newrange:

            if  (i % x) != 0 and  x not in lst:
                lst.append(x)



print (sum(lst))
print(lst)
