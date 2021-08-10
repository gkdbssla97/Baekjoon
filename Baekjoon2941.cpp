//
// Created by 하윤 on 2021/08/10.
// prob.2941

#include <stdio.h>
#include <string.h>

int main(void) {
    char str[101];
    scanf("%s", str);

    int len = strlen(str), cnt = 0;
    int tf;
    for (int i = 0; i < len; i++) {
        tf = 0;
        if (str[i] == 'c') {
            if (str[i + 1] == '=' || str[i + 1] == '-') {
                cnt++;
                tf = 1;
                i++;
            }
        } else if (str[i] == 'd') {
            if (str[i + 1] == '-') {
                cnt++;
                tf = 1;
                i++;
            }
            if (str[i + 1] == 'z')
                if (str[i + 2] == '=') {
                    cnt++;
                    tf = 1;
                    i+=2;
                }
        } else if (str[i] == 'l' || str[i] == 'n') {
            if (str[i + 1] == 'j') {
                cnt++;
                tf = 1;
                i++;
            }
        } else if (str[i] == 's' || str[i] == 'z') {
            if (str[i + 1] == '=') {
                cnt++;
                tf = 1;
                i++;
            }
        }
        if(tf == 0) cnt++;
    }
    printf("%d\n", cnt);

    return 0;
}






