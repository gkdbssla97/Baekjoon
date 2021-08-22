from math import *

def prime_num(x) :
    if x == 1 :
        return False
    for i in range(2, int(pow(x,0.5)+1)) :
        if(x % i == 0) :
            return False
    return True



while 1 :
    num = int(input())
    cnt = 0
    if num == 0 :
        break

    for i in range(num + 1, (num * 2) + 1) :
        if(prime_num(i)) :
            cnt += 1
    
    print(cnt)
