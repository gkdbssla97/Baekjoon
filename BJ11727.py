import sys

d = [0 for i in range(1001)]

d[1] = 1
d[2] = 3

N = int(sys.stdin.readline())
for i in range(3, N + 1):
    d[i] = d[i - 1] + (d[i - 2] * 2)
print(d[i] % 10007)