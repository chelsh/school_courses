# Exercise 1
print((2 + 11) / 5 ** 2 + 13 / 9 * 21 / 152)
print(310 ** (1/2))
print(4 ** (3 * 2))

# Exercise 2 
a = 3;b = 5;c = 2
print(   (  -b + (b ** 2 - 4*a*c) ** (1/2)   ) / 2*a)
print((b ** c) % a)
print((100 * a + 10 * b + c) // 7)

# Exercise 3 
answer = input("적중률 100% 심리 테스트를 시작합니다. \n당신은 중국음식점에 갔습니다. \n메뉴판에서 가장 먼저 보이는 것은? ")

print(f'''분석중...

당신은..\n{answer}\n을 좋아하는 타입입니다.''')



# Exercise 4

N = int(input("시간 입력 : "))
pay = int(N * 2 / 5 * 9160)
print(f"주휴수당 금액은 {pay}원입니다.")