inp = input('Enter a number: ')

int = int(inp) - 1
mylist = []
while int > 0:
    vartest3 = int % 3
    vartest5 = int % 5
    print(vartest3,vartest5)
    if vartest3 == 0 or vartest5 == 0:
        mylist.append(int)
    int = int - 1

print(mylist)
total = sum(mylist)
print (total)
