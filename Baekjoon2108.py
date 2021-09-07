import sys
from collections import Counter

N = int(sys.stdin.readline())

memo = []
for _ in range(N) :
    x = int(sys.stdin.readline())
    memo.append(x)

print(round(sum(memo) / N))
memo.sort()
print(memo.index(N//2))

cnt_memo = Counter(memo).most_common(2)
if cnt_memo[0][1] == cnt_memo[1][1] :
    print(cnt_memo[1][0])
else :
    print(cnt_memo[0][0])

print(max(memo) - min(memo))