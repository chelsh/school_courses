#include<stdio.h>

int main() {
    int N, i;
    
    scanf("%d", &N);
    printf("1");
    
    for(i = 2; i <= N; i++){
        if(N % i == 0){
            printf(" %d", i);
        }
    }
    
    return 0;
}