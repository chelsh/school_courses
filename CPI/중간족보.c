//대칭 정수 만들기
#include<stdio.h>

int main() {
    int N, M, cnt = 0, first = 1, min, max = 0;

    while (1) {
        scanf("%d", &N);

        if (N == 0)
            break;

        else {
            M = N;

            while (N > 0) {
                M *= 10;
                M += N % 10;
                N /= 10;
            }

            printf(" %d", M);

            if (first) {
                min = M;
                first = 0;
            }

            if (min > M) {
                min = M;
            }

            if (max < M) {
                max = M;
            }

            while (M > 0) {
                if (M % 10 == 5) {
                    cnt++;
                }
                M /= 10;
            }

            printf(" %d", cnt);
            cnt = 0;
        }
    }
    
    printf("\n%d %d", min, max);
    return 0;
}

//최댓값 구하기
#include<stdio.h>

int main() {
    int x[100];
    int i, cnt = 0, max;
    
    scanf("%d", &x[0]);
    max = x[0];
    
    for(i = 1; i < 100; i++){
        scanf("%d", &x[i]);
        
        if(x[i] == 0)
            break;
            
        cnt++;
    }
    
    for(i = 1; i <= cnt; i++){
        if(max < x[i])
            max = x[i];
    }
    
    printf("%d\n", max);
    
    for(i = 0; i <= cnt; i++){
        if(x[i] == max){
            printf(" %d", i);
        }
    }
    
    return 0;
}

//소수 출력하기
#include<stdio.h>

int main() {
    int N, i, is_prime, next, cnt = 0;
    
    while(1){
        scanf("%d", &N);
        if(N < 0)
            break;
        
        else{
            is_prime = 1;
            
            for(i = 2; i < N; i++){
                if(N % i == 0){
                    is_prime = 0;
                    break;
                }
            }
            
            if(is_prime){
                printf(" %d", N);
                cnt++;
                
                next = N;
                while(1){
                    next += 1;
                    is_prime = 1;
                    for(i = 2; i < next; i++){
                        if(next % i == 0)
                            is_prime = 0;
                            break;
                    }
                    
                    if(is_prime){
                        printf(" %d\n", next);
                        break;
                    }
                    
                }
            }
        }
    }
    
    if(cnt == 0)
        printf("none");
    return 0;
}

//