#2
N = int(input())
i = 1
result = 0
while i <= N ** (1 / 2):
    if N % i == 0:
        result += i
        if N != i * i:
            result += N / i
    i += 1
print("YES" if result == N * 2 else "NO")