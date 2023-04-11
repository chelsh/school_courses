#1
def pythagoras(L):
    L.sort()
    if L[2]**2 == L[0] ** 2 + L[1] ** 2:
        print("피타고라스 순서쌍입니다.")
    else:
        print("피타고라스 순서쌍이 아닙니다.")

triangle = []
for i in range(3):
    triangle.append(int(input()))
pythagoras(triangle)

#2
    #1 함수 정의 전에 호출 -> 에러
    #2 True
    #3 func_3은 반환만 하고 출력 X -> print(r)에서 10만 출력됨
    
    #답: 1번 

#3
def list_multi(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] * list_multi(L[1:])

input_list = [int(i) for i in input().split()]
print(list_multi(input_list))

#4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def comb(n, r):
    return factorial(n) / (factorial(n - r) * factorial(r))  

def stairs(n):
    result = 0
    q = n // 2
    for i in range(q + 1):
        result += comb(n, i)
        n -= 1
    return result 

N = int(input())
print(int(stairs(N)))

def f1():
    num1 = 50
    print(num2)
def f2():
    num2 = 70
    print(num2)
    f1()
num2 = 30
f2()
