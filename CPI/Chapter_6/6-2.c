#include<stdio.h>

int main() {
    int n, i, sum = 0, min, max;
    
    scanf("%d", &n);
    sum += n;
    min = n;
    max = n;
    
    while(n){
        scanf("%d", &n);
        if(n != 0){
            sum += n;
            
            if(min > n)
                min = n;
                
            if(max < n)
                max = n;
        }
    }
    
    printf("%d %d %d", sum, min, max);
    
    return 0;
}