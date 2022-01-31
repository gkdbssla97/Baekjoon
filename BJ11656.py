import sys

word = sys.stdin.readline().rstrip()

pick = []
result = []
for i in word:
    pick.append(word)
    word = word[1:]

for i in sorted(pick):
    print(i)

