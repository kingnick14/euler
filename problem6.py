inp = input('What range would you like to test?')
try:
    inp = int(inp) + 1
except:
    print('Please enter an integer!')
    exit()

ran = range(1,inp)
sq = 0
sumsq = 0

for i in ran:
    sq = i ** 2 + sq
    sumsq = i + sumsq

sumsq = sumsq ** 2

print(sumsq - sq)
