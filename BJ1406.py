import sys

word = list(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline())

cursor = len(word)
for i in range(num):
    cmd1 = (sys.stdin.readline().split())
    order = cmd1[0]
    print(list(cmd1))
    if order == "P":
        val = cmd1[1]
        word = word[0:cursor] + val + word[cursor:]
        cursor += 1
        #print(word[0:cursor-1])
    elif order == "L":
        if cursor != 0:
            cursor -= 1
    elif order == "D":
        if cursor != len(word):
            cursor += 1
    elif order == "B":
        if not cursor == 0:
            word = word[0:cursor] + word[cursor:]

print(word)

