import sys

N = int(sys.stdin.readline())

#dp = [[0 for _ in range(2)] for _ in range(91)]
# dp[1] = [0, 1] # 1
# dp[2] = [1, 0] # 10
# dp[3] = [1, 1] # 101 100
# dp[4] = [2, 1] 1000 1001 1010
# dp[5] = [4, 1] 10000 10101 10001 10010 10100
dp = [0 for _ in range(91)]
dp[1] = 1
dp[2] = 1
for i in range(3, N + 2):
    # dp[i][0] = (dp[i - 1][0]) * 2
    # dp[i][1] = dp[i - 1][1]
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N])

# 1 -> 0
# 0 -> 1, 0
# 1 1 2 3 5 8
# 2 1 1 2 2

