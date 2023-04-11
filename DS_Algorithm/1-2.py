# #page9 실습
# nums = [int(i) for i in input().split()]
# target = int(input())
# flag = False
# for i in range(len(nums) - 1):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             result = [i, j]
#             flag = True
#             break
#     if flag:
#         break
# print(result)
# print(f"Because nums[{result[0]}] + nums[{result[1]}] == {target}, we return {result}.")

# #page9 실습 코드예시 (page10)
# from typing import *
# import time
# def twoSum(data: List[int], target: int):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return [i, j]
# start = time.time()
# data = [3,1,7,4,8,9,10,2,11,15,18,21,22,14,6]
# target = 37
# result = twoSum(data, target)
# end = time.time()
# print(f'index where the sum of two numbers becomes {target}:: {result} ')
# print(f'run time :: {end-start}')

# #page16 filter 함수
# users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
#   {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
#   {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
#   {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
#   {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]

# def is_man(user):
#     return user['sex'] == 'M'

# print(list(filter(is_man, users)))

# #page17 enumerate 함수
# data = [3,1,7,4,8,9,10,2,11,15,18,21,22,14,6]
# result = list(enumerate(data))
# print(result)
# for i in result:
#     print(i)
# result = [ (i,value) for i, value in enumerate(data)]
# print(result)

# #page19 실습
# from typing import *
# def waterCal(person: int, water: int) -> List[int]:
#     pack = 12
#     total = person * water
#     pack = total // pack
#     item = total % 12
#     pay = pack * 10 ** 4 + item * 800
#     return [pack, item, pay]


# if __name__=="__main__":
#     person, water = [int(i) for i in input("enter the number of person and water >> ").split()]
#     result = waterCal(person, water)
#     print(f"{person}의 주문 생수는 {result[0]}팩과 {result[1]}개이며 금액은 {result[2]}")

# #page22 
# fact, n = 1, 0
# n = int(input("factorial 정수입력 >> "))
# for n in range(1, n+1):
#     fact *= n
#     print("n : %d, 누적곱: %d" % (n,fact))


#page23

# for i in range(10):
#     print("i: %d" % i)
#     # continue
#     print("%d의 거듭제곱: %d" % (i,i**2))

# #고객등급 프로그램
# #판매금액이 300이상이면 VIP, 아니면 Family
# membership = ''
# point = int(input('customer point >> '))
# if point >= 300:
#     membership = "VIP"
#     # break    --->  break는 항상 반복문 안에 있어야! 
# else:
#     membership = 'Family'
# print(f'customer membership is {membership}')

# #왼쪽의 고객등급 프로그램을 무한루프로 수정, point 변수에 음수가 입력되면 무한루프가 멈추도록 할 것
# while True:
#     point = int(input())
#     if point >= 300:
#         membership = "VIP"
#     elif point >= 0:
#         membership = "Family"
#     else:
#         break
#     print(f'customer membership is {membership}')

# #page24 실습
# #다음 turtle 모듈을 사용한 다각형 생성코드임, 이 코드를 반복문 구문으로 변경
# import turtle as t
# from random import choice
# color = ['darkred','sienna','ivory','lightgreen','gold','fuchsia','deeppink','crimson','olive','lime','midnightblue','lavender','blueviolet','plum','m','tan','darkorange','y','springgreen','coral','indianred','rosybrown','darkgray','teal']
# t.shape('turtle')
# t.pensize(5)
# for i in range(2, 12):
#     t.circle(i * 10, steps = i + 1)
#     t.color(choice(color))
# t.done()