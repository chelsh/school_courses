a = input()
b = input()
i = 2

while True:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        s = str(i)
        if a in s:
            if b in s:
                print(s)
                break
    i += 1