import math
import sys

r = 10000000
sieve = [True] * r

def prime(M):
    for i in range(2, int(math.sqrt(r)) + 1):
        if sieve[i] == True:
            for j in range(i * 2, M, i):
                sieve[j] = False

N = int(sys.stdin.readline())

i = 2
while 1:
    if N % i == 0:
        print(i)
        N /= i
    else:
        i += 1
    if N == 1:
        break


