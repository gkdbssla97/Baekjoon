//
// Created by 하윤 on 2021/08/18.
// prob.2581


#include <stdio.h>

int main(void) {
    int num1, num2;
    scanf("%d",&num1);
    scanf("%d",&num2);

    int min = 10001, sum = 0;
    int cnt = 0;
    for(int i = num1; i <= num2; i++) {
        int tf = 0;
        if(i == 1)
            continue;
        for(int j = 2; j < i; j++) {
            if(i % j == 0)
                tf = 1;
        } if(tf == 0) {
            cnt++;
            sum += i;
            if (min > i)
                min = i;
        }
    } if(cnt == 0) {
        printf("-1\n");
        return 0;
    }
    printf("%d\n%d\n",sum, min);

    return 0;
}



