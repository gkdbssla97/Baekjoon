//
// Created by 하윤 on 2021/08/10.
// prob.1316

#include <stdio.h>
#include <string.h>

int check(char str[], int len);

int main(void) {
    int num, tf;
    scanf("%d", &num);
    int result = num;
    char str[101];
    for(int i = 0; i < num; i++){
        scanf("%s",str);
        //getchar();
        int len = strlen(str);
        tf = check(str, len);
        if(tf == 0)
            result--;
    }
    printf("%d\n", result);

    return 0;
}

int check(char str[], int len) {
    int distance = 0;

    for(int i = 0; i < len; i++) {
        for(int j = 0; j < len; j++){
            if(str[i] == str[j]){
                distance = j - i;
                if(distance > 1){
                    if(str[j] != str[j-1])
                        return 0;
                }
            }
        }
    } return 1;
}