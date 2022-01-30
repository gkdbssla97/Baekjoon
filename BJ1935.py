import sys

M = int(sys.stdin.readline())
cal = sys.stdin.readline().rstrip()

pick = [0]*M
for i in range(M):
    pick[i] = int(sys.stdin.readline())

stack = []
a1 = 0
a2 = 0
for l in cal:
    #print(l)
    if l.isupper():
        stack.append(pick[ord(l) - ord('A')])
    else:
        a2 = stack.pop()
        a1 = stack.pop()
        if l == '+':
            stack.append(a1+a2)
        elif l == '-':
            stack.append(a1-a2)
        elif l == '*':
            stack.append(a1*a2)
        elif l == '/':
            stack.append(a1/a2)

print("{:.2f}".format(stack[-1]))
#print(list(pick))