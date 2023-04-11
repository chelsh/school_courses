#1
a = int(input())
b = int(input())
A = a; B = b
i = 1
while A <= B:
    if i % 2 != 0:
        A += 10000
    else:
        A *= 1.07
    B *= 1.02
    i += 1
print(i - 1)