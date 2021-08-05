//
// Created by 하윤 on 2021/08/01.
//prob.2908

#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable 4996)
#include <stdio.h>
#define MAX 1000001
#include <stdlib.h>
#include <string.h>

int main() {
    int a, b;
    scanf("%d %d",&a,&b);

    a = ((a % 10) * 100) + (((a / 10) % 10) * 10) + (a / 100);
    b = ((b % 10) * 100) + (((b / 10) % 10) * 10) + (b / 100);

    if(a > b)
        printf("%d\n",a);
    else
        printf("%d\n",b);

    return 0;
}