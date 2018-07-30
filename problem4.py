#def reverseEven(changeMe):
    changed = changeMe[:1]

import operator
pal = 0
count = 0
firsthalf = 0
secondhalf = 0
numbers = range(100,999)

for x in range(len(numbers)):
    for y in range(x+1,len(numbers)):
        multint = numbers[x]*numbers[y]
        multstr = str(multint)
        #print(len(multstr),'is the length of',multint)
        count += 1

        if len(multstr) % 2 == 0:
            firsthalf = int(len(multstr)/2)

            secondhalf = int(len(multstr)/2 * - 1)
            if len(firsthalf/2) % 2 == 0
                reversefirst =
                #list comprehention checking left and right, building a list in either direcion





            if multstr[:operator.__index__(firsthalf)] == multstr[operator.__index__(secondhalf):]:
                pal = multint
                print(pal)

print(count,'combos found')
print(pal)

        #print(mult,type(mult))
