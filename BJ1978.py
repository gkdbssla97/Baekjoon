import sys

M = int(sys.stdin.readline().rstrip())
pick = list(map(int, sys.stdin.readline().split()))

cnt, i = 0, 0
while i < M:
    flag = False
    for j in range(2, pick[i]):
        if pick[i] % j == 0:
            flag = True
            break
    if flag == False and pick[i] != 1:
        cnt += 1
    i += 1
print(cnt)