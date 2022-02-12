# 1 -> 1(1)
# 2 -> 11, 2(2)
# 3 -> 111,12,21,3(4)
# 4 -> 1111,112, 121, 211, 13, 31, 22(7)
# 5-> 11111, 1112(4), 122(3), 23(2), 113(3) ->(13)

def plus(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return plus(N-1) + plus(N-2) + plus(N-3)
import sys

M = int(sys.stdin.readline())

for _ in range(M):
    N = int(sys.stdin.readline().rstrip())
    print(plus(N))
