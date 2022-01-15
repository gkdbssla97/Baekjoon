import sys

M = int(sys.stdin.readline())

for i in range(M):
    sum = 0
    flag = 1
    VPS = list((sys.stdin.readline()).rstrip())
    print(VPS)
    for idx in VPS:
        if idx == '(':
            sum += 1
        elif idx == ')':
            sum -= 1
        if sum == -1:
            print("NO")
            flag = 0
            break
    if flag == 1:
        if sum == 0:
            print("YES")
        else :
            print("NO")

