import math
import sys

M = int(sys.stdin.readline())


for _ in range(M):
    total = 0
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            total += math.gcd(arr[i], arr[j])
    print(total)