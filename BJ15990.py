import sys

# 2차원 배열
dp = [[0 for i in range(3)] for j in range(100001)]

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]


M = int(sys.stdin.readline().rstrip())

for i in range(4, 100001):
    # +1 더했을 때 = +1마지막(x) + +2마지막 + +3마지막
    dp[i][0] = dp[i-1][1] % 1000000009 + dp[i-1][2] % 1000000009
    # +2 더했을 때 = +1마지막 + +2마지막(x) + +3마지막
    dp[i][1] = dp[i-2][0] % 1000000009 + dp[i-2][2] % 1000000009
    # +3 더했을 때 = +1마지막 + +2마지막 + +3마지막(x)
    dp[i][2] = dp[i-3][0] % 1000000009 + dp[i-3][1] % 1000000009

for i in range(M):
    N = int(sys.stdin.readline().rstrip())
    print(sum(dp[N]) % 1000000009)
