fibo = [1,2]
tab = 0

while True:
    fpo = len(fibo) - 1
    spo = len(fibo) - 2
    tab = fibo[fpo] + fibo[spo]
    if tab > 4000000: break
    fibo.append(tab)


print(fibo)
evens = []

for nb in fibo:
    rem = nb % 2
    if not rem == 0: continue
    evens.append(nb)

total = sum(evens)
print(total)
