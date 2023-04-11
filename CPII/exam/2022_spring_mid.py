#1
L = [int(n) for n in input().split()]
result = []
for i in range(len(L)):
    if L[i] > (sum(L) - L[i]) * 3 / (len(L) - 1) * 2:
        result.append(L[i])
if len(result) == 0:
    print("Not Found")
else:
    for i in result:
        print(i, end = " ")

#2
def TigerNumber(n):
    L = [int(i) for i in list(str(n))]
    result = 0
    i = 0
    while result == 0 and i < len(L):
        result = n % L[i]
        i += 1
        if result != 0:
            return False
    return True

#3 
L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
if len(L1) != len(L2) or len(set(L1)) != len(set(L2)):
    print("NO")
else:
    l = len(L1)
    for i in range(l - 1):
        for j in range(i + 1, l):
            if L1[i] > L1[j]:
                m = L1[i]
                L1[i] = L1[j]
                L1[j] = m
            if L2[i] > L2[j]:
                m = L2[i]
                L2[i] = L2[j]
                L2[j] = m
print("YES" if L1 == L2 else "NO")

#4
S = list(input())
L1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
L2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
L3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
for i in range(len(S)):
    if S[i] in L1:
        S[i] = 1
    elif S[i] in L2:
        S[i] = 2
    elif S[i] in L3:
        S[i] = 3
    else:
        S[i] = 4
result = 0
for i in range(len(S) - 1):
    d = S[i] - S[i + 1]
    if d >= 0:
        result += d
    else:
        result -= d
print(result)

__________________________________________________

1

origin = [3,5,4,1,2]
sorted(origin)
new = origin.sort(reverse = True)
print(new)
print(origin)
def f(n):
    if(n == 0) or (n == 1):
        return n
    else:
        print(n)
        return f(n-1)*f(n-2)
        print(n)

print("return" + str(f(5)))



#1
L = [int(i) for i in input().split()]
result = None

for item in L:
    avg = (sum(L) - item) / (len(L) - 1)
    if item > avg * 1.5:
        result = item

if result == None:
    print("Not Found")
else:
    print(result)
    

#2
def TigerNumber(n: int):
    s = str(n)
    nums = [int(i) for i in s]
    
    for i in nums:
        if n % i != 0:
            return False
    
    return True

#3
L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]

if len(L1) != len(L2):
    print("NO")

else:
    L1.sort()
    L2.sort()

    # for i in range(len(L1)):
    #     if L1[i] != L2[i]:
    #         print("NO")
    #         break
    if L1 != L2:
        print("NO")
    
    else:
        print("YES")



#4
L = [['q', 'w', 'e', 'r','t','y','u','i','o','p'], ['a','s','d','f','g','h','j','k','l'] ,['z','x','c','v','b','n','m'], [' ']]

sentence = input()
numList = []

for i in range(len(sentence)):
    for j in range(4):
        if sentence[i] in L[j]:
            numList.append(j)

sum = 0

for i in range(len(numList) - 1):
    d = numList[i] - numList[i+1]
    if d < 0:
        sum -= d
    else:
        sum += d

print(sum)