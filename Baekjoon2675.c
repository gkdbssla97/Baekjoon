//
// Created by 하윤 on 2021/07/29.
// prob.2675

#include <stdio.h>
#include <string.h>

int main(void) {
    int num, tmp;
    scanf("%d", &num);

    char str[21];
    char p[21];
    for(int i = 0; i < num; i++){
        int n = 0;
        scanf("%d",&tmp);
        scanf("%s",&str);
        for(int j = 0; j < strlen(str); j++){
            for(int k = 0; k < tmp; k++)
                p[n++] = str[j];

        }
        for(int a = 0; a < n; a++)
            printf("%c",p[a]);
        printf("\n");
    }
    return 0;
}

