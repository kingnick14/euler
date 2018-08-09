import math
a = 1
b = 1000
c = 1000000
squaresofc = []
rootsofc = []
# while True:
#     if math.sqrt(c)%1 == 0:
#         rootsofc.append(c)
#         squaresofc.append(int(math.sqrt(c)))
#     c -= 1
#     if c == 0 : break
#
# print("c is potentially:",rootsofc)
# print(squaresofc)


while True:
    if math.sqrt(a**2 + b**2)%1 == 0:
        print(a,b)
    a += 1
    b -= 1
    if a == 1001: break
