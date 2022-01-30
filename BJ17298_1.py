import sys

M = int(sys.stdin.readline())

pick = list(map(int, sys.stdin.readline().split()))
result = [-1] * M
#print(*result)
stack = []

stack.append(0)
for i in range(1, M):
    while stack and pick[stack[-1]] < pick[i]:
        #print(stack[-1])
        result[stack.pop()] = pick[i]
        #print("실행")
    stack.append(i)
print(*result)
# for i in range(M):
#     stack.push(pick[0])

