import math
import sys

N = int(sys.stdin.readline())

dp = [i for i in range(N + 1)]
dp[0] = 0
dp[1] = 1
# dp[4] = 1
# dp[5] = 2
# dp[6] = 3
# dp[7] = 4
for i in range(2, N + 1):
    for j in range(1, i):
        if i < j**2:
            break
        if dp[i] > dp[i - j**2] + 1:
            dp[i] = dp[i - j**2] + 1
print(dp[N])