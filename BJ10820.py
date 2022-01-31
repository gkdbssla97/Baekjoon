import sys

while 1:
    word = sys.stdin.readline().rstrip("\n")
    if not word: break
    small_letter = 0
    big_letter = 0
    num = 0
    space = 0
    for i in word:
        #if i >= 'a' and i <= 'z':
        if i.islower():
            small_letter += 1
        #elif i >= 'A' and i <= 'Z':
        elif i.isupper():
            big_letter += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            num += 1
    print(small_letter, big_letter, num, space)

