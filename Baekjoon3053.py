# 210825
# prob. 3053

pi = 3.14159265359
from math import *
# 택시 기하학 밑변의 길이와 높이가 R인 삼각형 4개의 넓이

import sys

radius = int(sys.stdin.readline())

print("{:.6f}" .format(pow(radius, 2) * pi))
print("{:.6f}" .format((pow(radius, 2) / 2) * 4 ))