//
// Created by 하윤 on 2021/07/29.
// prob.1157

#include <stdio.h>
#include <string.h>

int main(void) {
    char str[1000001];
    int cnt[26] = {0,};

    scanf("%s",&str);

    int len = strlen(str);
    for(int i = 'a'; i <= 'z'; i++){
        for(int j = 0; j <= len; j++)
            if(i == str[j])
                cnt[i - 'a']++;
    }
    for(int i = 'A'; i <= 'Z'; i++){
        for(int j = 0; j <= len; j++)
            if(i == str[j])
                cnt[i - 'A']++;
    }
    int max = 0;
    for(int i = 0; i < 26; i++){
        if(cnt[i] > max)
            max = cnt[i];
    }
    int c = 0,idx;

    for(int i = 0; i < 26; i++) {
        if (cnt[i] == max) {
            idx = i;
            c++;
        }
    }
    if(c <= 1)
        printf("%c\n", idx +'A');
    else
        printf("?\n");

    //printf("max: %d\n",idx + 'A');
    return 0;
}

