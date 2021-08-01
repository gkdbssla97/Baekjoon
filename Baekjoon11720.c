//
// Created by 하윤 on 2021/07/28.
//prob.11720

#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable 4996)
#include <stdio.h>

int main() {
    int num, sum = 0;
    scanf("%d",&num);

    char arr[num];
    scanf("%s",&arr);
    for(int i = 0; i < num; i++)
        sum += arr[i] -48;

    printf("%d\n", sum);

    return 0;
}