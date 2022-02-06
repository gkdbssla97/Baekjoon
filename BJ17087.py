import math
import sys

N, S = map(int, sys.stdin.readline().split())

pick = list(map(int, sys.stdin.readline().split()))
a = []
for i in pick:
    #print(i - S)
    a.append(abs(i - S))

d = min(a)
for i in a:
    d = math.gcd(i, d)
print(d)