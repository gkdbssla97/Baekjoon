//
// Created by 하윤 on 2021/07/24.
//prob.10809

#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable 4996)
#include <stdio.h>
#include <string.h>

int main() {
    char str[101];
    char ap[27] = {'a','b','c','d','e','f','g','h',
                   'i','j','k','l','m','n','o','p',
                   'q','r','s','t','u','v','w','x',
                   'y','z'};
    scanf("%s",&str);
    int flag = 0, j;
    printf("strlen: %d \n sizeof: %d \n",strlen(ap), sizeof(str));
    for(int i = 0; i < 26; i++){
        for(j = 0; j < strlen(str); j++) {
            if (ap[i] == str[j]) {
                printf("%d ", j);
                flag = 1;
                break;
            }
        }
        if(flag == 0) // 알파벳 없음
            printf("%d ", -1);
        flag = 0;
    }

    return 0;
}