import sys

M = int(sys.stdin.readline())

pick = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(M):
    flag = False
    for j in range(M):
        #print(f'i:{i}값, j:{i+1}값')
        if i < j and pick[i] < pick[j]:
            result.append(pick[j])
            #print(f'pick{j}')
            flag = True
            break
    if flag == False:
        result.append(-1)
print(list(result))