#include<stdio.h>

int main(){
    float a, b;
    
    printf("첫 번째 수: ");
    scanf("%f", &a);
    printf("두 번째 수: ");
    scanf("%f", &b);
    
    printf("합: %f", a + b);
    return 0;
}