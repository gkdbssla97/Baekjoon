import sys
import math

N, M = map(int, sys.stdin.readline().split())
#print(N, M)
def cnt(x, y):
    cnt= 0
    while x != 0:
        x //= y
        cnt += x
    return cnt

five_cnt = cnt(N, 5) - cnt(M, 5) - cnt(N-M, 5)
two_cnt = cnt(N, 2) - cnt(M, 2) - cnt(N-M, 2)

result = min(five_cnt, two_cnt)
print(result)