#include<stdio.h>

int main() {
    int X, result = 0;
    
    scanf("%d", &X);
    
    while (X > 0){
        result *= 10;
        result += X % 10;
        X /= 10;
    }
    
    printf("%d", result);
    
    return 0;
}