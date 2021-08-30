# 210830
# prob. 2798

import random, sys

N, M = map(int, input().split())

memo = list(map(int, input().split()))

max1 = 0

for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            if(memo[i] + memo[j] + memo[k] > M) :
                continue
            else :
                max1 = max(max1, memo[i] + memo[j] + memo[k])

print(max1)