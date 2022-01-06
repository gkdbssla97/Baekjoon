from collections import deque

N, M = map(int, input().split())

# for _ in range(N):
#     house = input().split()
house = [input() for _ in range(N)]
#print(house)
cnt = 0
for i in range(N):
    pre = '/'
    for j in range(M):
        if house[i][j] == '-':
            if house[i][j] != pre:
                cnt += 1
        pre = house[i][j]

#print(cnt)
for i in range(M):
    pre = '/'
    for j in range(N):
        if house[j][i] == '|':
            if house[j][i] != pre:
                cnt += 1
        pre = house[j][i]

print(cnt)



