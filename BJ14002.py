import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
t = max(dp)
print(t) # 4
# print(dp)
pick = []
for i in range(N-1, -1, -1):
    if t <= 0:
        break
    if dp[i] == t:
        #print(arr[i])
        pick.append(str(arr[i]))
        t -= 1
print(" ".join(reversed(pick)))
#print("안경 잘어울린다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")