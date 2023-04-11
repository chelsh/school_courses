A = [None, 1, 2, 3]

def Y(i):
    if i == 3:
        print(A)
    else:
        Y(i + 1)
        for j in range(i + 1, 3 + 1):
            A[i], A[j] = A[j], A[i]
            Y(i + 1)
            A[i], A[j] = A[j], A[i]

Y(1)