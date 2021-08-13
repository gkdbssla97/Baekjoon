//
// Created by 하윤 on 2021/08/13.
// prob.2869

#include <stdio.h>

int main(void) {
    int A, B, V;

    int height = 0, day = 1;
    scanf("%d %d %d",&A, &B, &V);

    printf("%d\n",(V - B - 1) / ( A - B) + 1);


    return 0;
}

