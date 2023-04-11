#1
N = int(input())
rt = 0          # rt = 'return'
while N >= 3:
    bonus = N // 3
    N = N % 3 + bonus
    rt += 3 * bonus
print(N + rt)

#1 (수학적 풀이)
N = int(input())
print(N + (N - 1) // 2)

#2
L = []
while True:
    bev = input()
    if bev == "END":
        break
    else:
        L.append(bev)
lenL = len(L)
for i in range(lenL):
    l = L[i].split()
    abb = ""
    for j in range(len(l)):
        abb += l[j][0]
    L[i] = abb
flag = False
for i in range(lenL):
    if L[i] in L[i + 1:]:
            print("YES")
            flag = True
            break
if flag == False:
    print("NO")

#3
L = []
while True:
    dnp = input().split()     # dnp = destination & price
    if dnp[-1].isdigit() == True:
        L.append(dnp)
    else:
        destination = dnp
        break
P = []
for item in L:
    if item[:-1] == destination:
        item[-1] = int(item[-1])
        P.append(item[-1])
print(min(P))


#버블 정렬
numbers = [3,8,4,2,6,1,9]

i = 1
length = len(numbers)

while i < length:
    j = 0
    while j < length - i:
        if (numbers[j] > numbers[j+1]):
            numbers[j],numbers[j+1] = numbers[j + 1], numbers[j]
        j += 1
    i += 1

print(numbers)

#삽입 정렬

i = 1
length = len(numbers)

while i < length:
    j = i - 1
    key = numbers[i]
    while j <= 0:
        if key < numbers[j]:
            numbers[j+1]