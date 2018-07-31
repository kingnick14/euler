import time

num = 0
done = False

start = time.time()
try:
    while True:
        num += 20
        for i in range(20,2,-1):
            if not num % i == 0: break

            if i < 10: print(num,'is divisible by', i)
            if i == 3:
                elapsed = time.time() - start
                print(num,'is evenly divisible by 1 to 20 and took',elapsed,'seconds')
                done = True
        if done == True: break
except KeyboardInterrupt:
    print(num)
