import sys

N = int(sys.stdin.readline())
case = list(map(int, sys.stdin.readline().split()))
reverse_case = case[::-1]

ASC = [1 for i in range(N)]
DESC = [1 for j in range(N)]

for i in range(N):
    for j in range(i):
        if case[j] < case[i]:
            ASC[i] = max(ASC[i], ASC[j] + 1)
        if reverse_case[j] < reverse_case[i]:
            DESC[i] = max(DESC[i], DESC[j] + 1)

result = [0 for i in range(N)]
for i in range(N):
    result[i] = ASC[i] + DESC[N - i - 1] - 1
print(max(result))
