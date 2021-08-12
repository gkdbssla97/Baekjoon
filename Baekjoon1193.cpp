//
// Created by 하윤 on 2021/08/12.
// prob.1193

#include <stdio.h>

int main(void) {
    int num;
    scanf("%d",&num);

    int tmp = 1, idx = 1;
    if(num == 1) {
        printf("1/1\n");
        return 0;
    }
    for(int i = 2; i <= num; i++){
        tmp += i;
        if(tmp >= num){
            idx = i;
            break;
        }
    }
    if(idx % 2 != 0) {
        tmp = tmp - idx + 1;
        int dist = num - tmp;
        //printf("idx:%d\ntmp:%d\n", idx, tmp);
        //printf("dist:%d\n", dist);
        printf("%d/%d\n", (idx - dist), (1 + dist));
    } else {

        int dist = tmp - num;
        printf("idx:%d\ntmp:%d\n", idx, tmp);
        printf("dist:%d\n", dist);
        printf("%d/%d\n", (idx - dist), (1 + dist));
    }



    return 0;
}

