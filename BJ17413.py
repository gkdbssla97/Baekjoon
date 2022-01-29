import sys
word = list(sys.stdin.readline().rstrip())

start = 0
i = 0

while i < len(word):
    if word[i] == "<":
        i += 1
        while word[i] != ">":
            i += 1
        i += 1
    elif word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        sen = word[start:i]
        sen.reverse()
        word[start:i] = sen
    else:
        i += 1
    #print(i)
print("".join(word))
