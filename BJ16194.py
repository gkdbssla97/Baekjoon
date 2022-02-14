import sys

N = int(sys.stdin.readline())

pick = [0]
pick += list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(N + 2)]
dp[1] = pick[1]
dp[2] = min(pick[2], dp[1]*2)

for i in range(3, N+1):
    dp[i] = pick[i]
    for j in range(1, i // 2 + 1):
        dp[i] = min(dp[i], dp[i - j] + dp[j])
print(dp[N])
# Bottom - up type