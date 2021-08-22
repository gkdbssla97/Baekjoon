//
// Created by 하윤 on 2021/08/22.
// prob.4948
#include <stdio.h>
#include <math.h>

int main(void) {
    int num;
    int prime[246913] = {0, };
    prime[0] = 1, prime[1] = 1;
    for(int i = 2; i < 246913 / i; i++) {
        //if(prime[i] == 1) continue;
        for(int j = i * i; j < 246913; j += i) {
            if(j % i == 0)
                prime[j] = 1;
        }
    } int cnt;

    while(1) {
        scanf("%d", &num);
        if(num == 0)
            break;
        cnt = 0;
        for(int i = num + 1; i <= num * 2; i++) {
            if (prime[i] == 0)
                cnt++;
        }
        printf("%d\n",cnt);

    }
    return 0;
}

