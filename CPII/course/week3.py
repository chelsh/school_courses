#Exercise 1
area = int(input())
if area <= 49:
    print("청년")
elif area <= 69:
    print("신혼부부")
elif area <= 89:
    print("일반가구")
else:
    print("노년층")

# Exercise2
distance, time = [int(input()), input()]
def taxi(d, t):
    h = int(t[:2])
    charge = 0
    if d <= 3:
        charge = 4000
    else:
        charge = 4000 + (d - 3) * 500
    if h == 11 or 0 <= h <= 3:
        charge *= 1.2
    return charge
print(taxi(distance, time))

# Exercise3
adult = int(input("성인 고객 수를 입력하세요 : "))
child = int(input("아동 고객 수를 입력하세요 : "))
total = adult * 15 + child * 8
weight = int(input("수하물 무게(kg)을 입력하세요 : "))
if adult > 0:
    if total > 40:
        print("위탁 불가합니다.")
    elif total >= weight:
        print("위탁 가능합니다.")
    elif total < weight:
        print("위탁 불가합니다.")
else:
    print("위탁 불가합니다.")