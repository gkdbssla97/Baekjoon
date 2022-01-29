import sys
from collections import deque

M = int(sys.stdin.readline())
cmd = []
result = deque()
for _ in range(M):
    cmd = (sys.stdin.readline().split())
    if cmd[0] == "push_back":
        result.append(cmd[1])
    elif cmd[0] == "push_front":
        result.appendleft(cmd[1])
    elif cmd[0] == "pop_front":
        if result:
            print(result.popleft())
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if result:
            print(result.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(result))
    elif cmd[0] == "empty":
        if result:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if result:
            print(result[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if result:
            print(result[-1])
        else:
            print(-1)

    #print(result)
