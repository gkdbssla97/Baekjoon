import math
import sys

M, N = map(int, sys.stdin.readline().split())

cnt = 0
i = M
while i <= N:
    if i == 1:
        continue
    else:
        flag = False
        tmp = int(math.sqrt(i))
        for j in range(2, tmp + 1):
            if i % j == 0:
                flag = True
                break
        if flag == False:
            print(i)
    i += 1