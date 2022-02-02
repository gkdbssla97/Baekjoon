import math

n = 10000000
sieve = [True] * n

m = int(math.sqrt(n))
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i*2, n, i):
            if sieve[j] == True:
                sieve[j] = False

import sys
#print(sieve[])

while 1:
    M = int(sys.stdin.readline())
    if M == 0:
        break

    flag = False
    for i in range(3, n):
        if sieve[i] == True and sieve[M - i] == True:
            print(f'{M} = {i} + {M - i}')
            flag = True
            break
    if flag == False:
        print("Goldbach's conjecture is wrong.")