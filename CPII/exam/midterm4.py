x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

flag = 0

for i in range(len(x)):
    X = x[i]
    Y = y[i]
    xL =[]
    yL = []
    for _ in range(len(x)):
        xL.append(x[_])
    for _ in range(len(y)):
        yL.append(y[_])
    del xL[i]
    del yL[i]
    
    for j in range(len(xL)):
        d = ((x[i] - xL[j]) ** 2 + (y[i] - yL[j]) ** 2) ** (1/2)
        if d < 50:
            print("YES")
            flag = 1
            break
    
    if flag == 1:
        break

if flag == 0:
    print("NO")

L = [None] * 3
print(L)