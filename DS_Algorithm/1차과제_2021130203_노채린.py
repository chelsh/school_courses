l, T = [int(n) for n in input().split()]
L = [int(n) for n in input().split()]
result = []
for _ in range(T):
    i, j = [int(n) for n in input().split()]
    sum = 0
    for num in range(i - 1, j):
        sum += L[num]
    result.append(sum)

print(f"[result]\n{result[0]}\n{result[1]}")