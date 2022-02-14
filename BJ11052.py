import sys

M = int(sys.stdin.readline())
pick = [0]
pick += list(map(int, sys.stdin.readline().split()))
#print(pick)

dp = [0 for i in range(M + 2)]
dp[1] = pick[1]
dp[2] = max(pick[2], pick[1]*2)

for i in range(3, M + 1):
    dp[i] = pick[i]
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
print(dp[i])