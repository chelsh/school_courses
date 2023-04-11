# Exercise1
N = int(input())
for i in range(1, N):
    print("*" * i)


# Exercise2
n = int(input("수를 입력하세요 : "))  # input()으로 입력 받은 거는 문자열이니까 정수형으로 전환("int()"로 묶어주면 됨)
while n != 1:           # n이 1이 되기 전까지 반복
    if n % 2 == 0:      # n이 짝수일때 (2로 나눴을때 나머지가 0)
        n /= 2          # 2로 나눈다
    else:               # 짝수인 경우의 else이므로 홀수인 경우
        n = n * 3 + 1   # 3곱하고 1더하기
    print(int(n))       #출력 (근데 나누기 때문에 실수형으로 바뀌어서 1.000000 이런식으로 나오니까 정수형으로 바꿔서 출력)

# Exercise3
L = []
n = 0
while n >= 0:
    n = int(input())
    if n >= 0:
        L.append(n)
print(f"최고 매출액 : {max(L)}\n최저 매출액 : {min(L)}")

# Exercise4
print("Python 만보기")
total = 0
for i in range(1, 11):
    print(f"오늘 {i} 보 걸었어요.")
    total += i
    i += 1
print(f"지금까지 총 {total} 보 걸었네요!")


# Exercise5
num = int(input())   # N >= 2
for i in range(2, num):
    if num % i == 0:
        print("소수가 아닙니다.")
        break
else:
    print("소수입니다.")