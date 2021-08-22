from math import *

def prime_num(x) :
    if x == 1 :
        return False
    for i in range(2, int(pow(x,0.5)+1)) :
        if(x % i == 0) :
            return False
    return True

all_list = list(range(2,246912))
memo = []

for i in all_list:
    if prime_num(i) :
        memo.append(i)

num = int(input())

while 1 :
    cnt = 0
    if num == 0 :
        break

    for i in memo :
        if(num < i <= num * 2) :
            cnt += 1
    
    print(cnt)
    num = int(input())
