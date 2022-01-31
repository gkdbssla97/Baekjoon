import sys

A, B, C, D = map(int, sys.stdin.readline().split())

#print(A, B, C, D)
a1 =""
a2 =""
a1 += str(A) + str(B)
a2 += str(C) + str(D)
result = int(a1) + int(a2)
print(result, a1, a2)