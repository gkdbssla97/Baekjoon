//
// Created by 하윤 on 2021/08/14.
// prob.2775

#include <stdio.h>

int main(void) {
    int test;
    scanf("%d",&test);

    int n,k;
    int arr[15];

    for(int i = 0; i < test; i++){
        scanf("%d",&k); // 층
        scanf("%d",&n); // 호
        for(int i = 0; i < 14; i++)
            arr[i] = i + 1;
        for(int j = 0; j < k; j++){
            for(int q = 1; q < n; q++){
                arr[q] = arr[q - 1] + arr[q];
            }
        } printf("%d\n",arr[n-1]);
    }


    return 0;
}

