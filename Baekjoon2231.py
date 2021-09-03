import sys

num = int(sys.stdin.readline())

for i in range(1,num+1) :
    memo = map(int,str(i))
    if i + sum(memo) == num :
        print(i)
        break