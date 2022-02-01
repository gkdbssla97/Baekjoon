import sys

M = int(sys.stdin.readline())

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    if A < B:
        A, B = B, A
    a, b = A, B
    #print(A, B)
    while B != 0:
        A = A % B
        A, B = B, A
    print(a * (b//A))