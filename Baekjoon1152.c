//
// Created by 하윤 on 2021/08/01.
//prob.1152

#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable 4996)
#include <stdio.h>
#define MAX 1000001
#include <stdlib.h>
#include <string.h>

int main() {
    char str[MAX];
    scanf("%[^\n]",str);

    int len = strlen(str);
    int i = 0,cnt = 0;
    if(len == 1) {
        if (str[i] == ' ') {
            printf("0");
            return 0;
        }
    }
    while(i < len - 1){
        if(str[i] == ' ')
            cnt++;
        i++;

    } printf("%d",cnt+1);

    return 0;
}