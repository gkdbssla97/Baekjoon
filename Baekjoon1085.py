# 210825
# prob. 1085

import sys

x, y, w, h = map(int, input().split())
# y = int(sys.stdin.readline())
# w = int(sys.stdin.readline())
# h = int(sys.stdin.readline())

min_x = int(min(x, w-x))
min_y = int(min(y, h-y))

result = min(min_x,min_y)
print(result)