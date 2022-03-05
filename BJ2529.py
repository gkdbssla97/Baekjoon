import sys

K = int(sys.stdin.readline())
pick = list(map(str, sys.stdin.readline().split()))

check = [False] * 10
mn, mx = "", ""

def possible(i, j, pick):
    if pick == '<':
        #print(i < j)
        return i < j
    elif pick == '>':
        return i > j

def solve(cnt, z):
    global mx, mn
    if cnt == K + 1:
        if not len(mn):
            mn = z
        else:
            mx = z
        return
    for i in range(10):
        if not check[i]:
            if cnt == 0 or possible(z[-1], str(i), pick[cnt - 1]):
                #print(z + str(i))
                check[i] = True
                solve(cnt + 1, z + str(i))
                check[i] = False
solve(0, "")
print(mx)
print(mn)



