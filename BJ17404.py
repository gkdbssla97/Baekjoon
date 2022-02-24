from sys import maxsize
import sys

N = int(sys.stdin.readline().rstrip())
INF = maxsize
#dp = [[0] * 3 for _ in range(N + 1)]
RGB = [[0] * 3 for _ in range(N + 1)]

dp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = INF
for first in range(3):
    for j in range(3):
        if j == first:
              RGB[0][j] = dp[0][j]
        else:
            RGB[0][j] = INF
    for i in range(1, N):
        RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + dp[i][0]
        RGB[i][1] = min(RGB[i - 1][2], RGB[i - 1][0]) + dp[i][1]
        RGB[i][2] = min(RGB[i - 1][1], RGB[i - 1][0]) + dp[i][2]
    for k in range(3):
        if first == k:
            continue
        answer = min(answer, RGB[N - 1][k])
print(answer)