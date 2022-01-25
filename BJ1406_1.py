import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

num = int(sys.stdin.readline().rstrip())

for _ in range(num):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif cmd[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif cmd[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(cmd[1])
    print(st1, st2)
st1.extend(reversed(st2))
word = "".join(st1)
print(word)
