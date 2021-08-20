//
// Created by 하윤 on 2021/08/20.
// prob.1929

#include <stdio.h>
#include <math.h>

int main(void) {
    int N, M;
    scanf("%d %d",&N, &M);

    for(int i = N; i <= M; i++) {
        int tf = 0;
        int sqr = (int)sqrt(i);
        for(int j = 2; j <= sqr; j++) {
            if(i % j == 0)
                tf++;
        }
        if(tf == 0 && i != 1)
            printf("%d\n", i);
    }
    return 0;
}

