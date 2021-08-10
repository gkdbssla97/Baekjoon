//
// Created by 하윤 on 2021/08/09.
// prob.1712

#include <stdio.h>
#define INF 2147000000

int main(void){
    int A;
    int B;
    int C;

    int tf = 0, tmp;
    scanf("%d %d %d",&A,&B,&C);

    if(B >= C)
        printf("-1\n");
    else
        printf("%d\n",A / (C - B) + 1 );

    return 0;
}

