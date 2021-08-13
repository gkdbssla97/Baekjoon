//
// Created by 하윤 on 2021/08/13.
// prob.10250

#include <stdio.h>

int main(void) {
    int test;
    int h, w, n;
    int room;

    int tmp1, tmp2;
    scanf("%d",&test);
    for(int i = 0; i < test; i++) {
        scanf("%d %d %d", &h, &w, &n);
        tmp1 = n % h; // 층
        tmp2 = n / h + 1; // 호
        if (n % h == 0)
            printf("%d%02d\n", h, n / h);
        else
            printf("%d%02d\n", tmp1, tmp2);
    }



    return 0;
}

