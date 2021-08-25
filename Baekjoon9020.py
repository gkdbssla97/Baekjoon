# Using Sieve of Eratosthenes
# 210825
# prob. 9020 
import sys 
from math import *

def prime(n) :
    prime_num = [True] * n
    for i in range(2, int(pow(n,0.5) + 1)) :
        if prime_num[i] == True :
            for j in range(2 * i, n, i) :
                prime_num[j] = False
    return [i for i in range(2, n) if prime_num[i] == True]

p = prime(10001)
n = int(sys.stdin.readline())

for i in range(n) :
    m = int(sys.stdin.readline())
    diff = 10001
    a = 0
    b = 0
    for j in range(len(p)) :
        if p[j] >= m / 2 :
            if m - p[j] in p :
                a = p[j]
                b = m - p[j]
                break
    print(b, a) 
