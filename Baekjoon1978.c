//
//
// Created by 하윤 on 2021/08/17.
// prob.1978

#include <stdio.h>

int main(void) {
    int num;
    scanf("%d",&num);

    int prime, cnt = 0;
    for(int i = 0; i < num; i++) {
        scanf("%d",&prime);
        int tf = 0;
        if(prime == 1)
            continue;
        for(int j = 2; j < prime; j++) {
            if(prime % j == 0)
                tf = 1;
        } if(tf == 0)
            cnt++;
    } printf("%d\n",cnt);

    return 0;
}