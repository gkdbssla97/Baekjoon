//
// Created by 하윤 on 2021/08/11.
// prob.2292

#include <stdio.h>

int main(void) {
    int num;
    scanf("%d",&num);

    int tmp = 1;
    if(num == 1) {
        printf("1\n");
        return 0;
    }
    for(int i = 1; i <= num; i++){
        if(num < tmp + (i * 6)) {
            printf("%d\n", i + 1);
            break;
        }
        tmp += i * 6;
    }



    return 0;
}

