import sys

word = sys.stdin.readline().rstrip()
result = [-1] * 26

for i in range(len(word)):
    if result[ord(word[i]) - ord('a')] == -1:
        result[ord(word[i]) - ord('a')] = i
print(*result)

#ord에 대해서 TIL 