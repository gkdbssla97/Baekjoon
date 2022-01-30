import sys
from collections import deque
cmd = list(sys.stdin.readline().rstrip())

a = []
b = []

flag = False
for i in cmd:
    if i.isalpha():
        a.append(i)
    else:
        if i == "(":
            b.append(i)
        elif i == '*' or i == '/':
            while b and (b[-1] == "*" or b[-1] == "/"):
                a.append(b.pop())
            b.append(i)
        elif i == '+' or i == "-":
            while b and b[-1] != "(":
                a.append(b.pop())
            b.append(i)
        elif i == ")":
            while b and b[-1] != "(":
               a.append(b.pop())
            b.pop()
while b:
    a.append(b.pop())
print("".join(a))
#print(a)


