import math
import sys

M = int(sys.stdin.readline().rstrip())

result = math.factorial(M)
#print(str(result)[::-1])
cnt = 0
for i in str(result)[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
