import sys

M = int(sys.stdin.readline())

block = []
for i in range(M):
    cmd = sys.stdin.readline().split()
    order = cmd[0]

    if order == "push":
        num = cmd[1]
        block.append(num)
    elif order == "top":
        if len(block) == 0:
            print("-1")
        else:
            print(block[-1])
        #print(block)
    elif order == "size":
        print(len(block))
    elif order == "empty":
        if len(block) == 0:
            print("1")
        else:
            print("0")
    elif order == "pop":
        if len(block) == 0:
            print("-1")
        else:
            print(block.pop())