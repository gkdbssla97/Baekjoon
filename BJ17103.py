import math
import sys

sieve = [True] * 1000000
sieve[1] = False
for i in range(2, int(math.sqrt(1000000)) + 1):
    if sieve[i] == True:
        for j in range(i * 2, 1000000, i):
            sieve[j] = False

def prime(M):
    cnt = 0
    for i in range(2, (M//2) + 1):
        #print(sieve[i], i)
        if (sieve[i] == True and sieve[M - i] == True):
            cnt += 1
            #print(i, M-i)
    print(cnt)

M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    num = int(sys.stdin.readline().rstrip())
    prime(num)

