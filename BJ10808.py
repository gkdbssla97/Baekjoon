import sys

word = sys.stdin.readline().rstrip()

cnt = [0] * 26

for i in word:
    print(ord(i), ord('a'))
    cnt[ord(i) - ord('a')] += 1

print(*cnt)

