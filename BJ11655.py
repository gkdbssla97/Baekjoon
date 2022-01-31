import sys

word = sys.stdin.readline().rstrip()
result = ""
for i in word:
    if i.isupper():
        if chr(ord(i) + 13) > "Z":
            result += chr(ord(i) - 13)
        else:
            result += chr((ord(i) + 13))
    elif i.islower():
        if chr(ord(i) + 13) > "z":
            result += chr(ord(i) - 13)
        else:
            result += chr((ord(i) + 13))
    else:
        result += i
print(result)