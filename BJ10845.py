import sys

M = int(sys.stdin.readline().rstrip())
st = []
for _ in range(M):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "push":
        st.append(cmd[1])
    elif cmd[0] == "front":
        if st:
            print("".join(st[0]))
        else:
            print(-1)
    elif cmd[0] == "back":
        if st:
            print(st[-1])
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(st))
    elif cmd[0] == "empty":
        if st:
            print(0)
        else:
            print(1)
    elif cmd[0] == "pop":
        if st:
            # st.reverse()
            # print(st.pop())
            # st.reverse()
            print(st.pop(0))
        else:
            print(-1)