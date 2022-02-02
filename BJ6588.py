import sys
import math

while 1:
    stack = []
    M = int(sys.stdin.readline())
    if M == 0:
        break
    for i in range(M):
        if i == 1:
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            if i % 2 != 0:
                stack.append(i)
    max = 0
    a, b = 0, 0
    for i in stack:
        for j in stack:
            if i == j:
                continue
            if M == i + j:
                if max < j - i:
                    max = j - i
                    a, b = i, j

    print(f'{M} = {a} + {b}')
