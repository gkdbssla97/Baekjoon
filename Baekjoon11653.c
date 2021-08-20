//
// Created by 하윤 on 2021/08/20.
// prob.11653

#include <stdio.h>

int main(void) {
    int num;
    scanf("%d",&num);
    if(num == 1)
        return 0;

    int i = 2;
    while(1) {
        if(num % i == 0) {
            num /= i;
            printf("%d\n", i);
        }
        else
            i++;
        if(num == 1)
            break;
    }

    return 0;
}

