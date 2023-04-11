# #page6 
# str_data = input("enter a sentence :: ")  #"happy birthday python" 입력
# print(str_data)
# #공백기준 분할하여 리스트로 저장
# str_list = str_data.split()    
# print(str_list)                 # ['happy', 'birthday', 'python']
# #기타 문자열관련 함수
# print(str_data.count('p'))      # 3
# print(str_data.upper())         # HAPPY BIRTHDAY PYTHON
# print(str_data)                 # happy birthday python 
# print(str_data.replace('python', 'Korea'))   # happy birthday Korea


# #page8 리스트 컴프리헨션
# """
# 1~ 100 사이의 값 중에서 3의 배수값들을 리스트로 생성
# """
# data = [ i for i in range(1, 101) if i % 3 == 0]
# print(data)
# """
# 1~20 값 중에서 짝수는 "even", 홀수는 "odd" 로 리스트 생성
# """
# data = [ "even" if i % 2 == 0 else "odd" for i in range(1,21)]
# print(data)

# import random
# #random.seed(777)
# data = [ random.randint(1,10000) for i in range(20)] #randrange(1,10001)
# print(data)
# """
# 랜덤 발생되는 값을 고정으로 하고 싶다면
# random.seed(정수값) 을 사용
# """


# #page 18~19 실습
# import random
# from typing import*

# def guess(com_n: set) -> List[bool]:
#     result = []
#     for i in range(3):
#         n = int(input("Enter the number 1 to 30 >> "))
#         if n in com_n:
#             result.append(True)
#         else:
#             result.append(False)
#     return result

# if __name__=="__main__":
#     com_n = set()
#     while True:
#         if len(com_n) == 3:
#             break
#         com_n.add(random.randint(1, 30))
#     result = guess(com_n)

#     if sum(result) == 3:        # True -> 1, False -> 0 !!!
#         print("You Win!!!")
#     else:
#         print(f"result:: {result}")
#         print(f"computer:: {com_n}")

# #page 20
# def odd_even(num: int):     # Type Hint
#     if not num.isdecimal() or num.isalpha():
#         return '입력값 오류'
#     num = int(num)
#     if num % 2 == 0:
#         return f'{num}은 짝수'
#     else:
#         return f'{num}은 홀수'

# if __name__ == "__main__":
#     number = input("enter integer >> ")
#     print(odd_even()) # 함수 호출

# # page 23  매개변수 종류
# # 일반 매개변수
# def add(num1: int, num2: int) -> int:
#     result = num1 + num2
#     return result
# print(add(2, 5))
# # 가변 매개변수 - 튜플
# def add(*nums: int):
#     result = sum(nums)
#     print(nums)       # (1, 2, 3, 4, 5): tuple
#     return result
# print(add(1,2,3,4,5))
# # 가변 매개변수 - 딕셔너리
# def add(**var: int):
#     print(var)          # {'first': 15, 'second': 2}
#     print(var.values())     # dict_values([15, 2])  : dict_values 클래스로 반환
#     result = sum(var.values())
#     return result
# print(add(first = 15, second = 2))  # 17
# 키워드 매개변수
# def add(second, *nums, first = 5, **dictNums):     #키워드 매개변수는 일반 매개변수의 항상 뒤에 위치!!
#     print(second)
#     print(nums)
#     print(dictNums)
#     result = first + second + sum(nums) + sum(dictNums.values())
#     return result
# print(add(1, 2, 3, 4, 5, 6, 7, first = 1, f=5,se=6,th = 3))   #TypeError: add() got multiple values for argument 'second'


# #page 24
# def grade(name, number=1, **points):
#     avg = sum(points.values())/len(points)
#     print(f'{name}은 학번 {number}이며 평균은 {avg:.2f}')
#     return avg
# if __name__ == "__main__":
#     average = grade('홍길동', 국어=90,영어=89,수학=77)
#     if average >= 90:
#         print('등급은 A')
#     elif average >= 80:
#         print('등급은 B')
#     elif average >= 70:
#         print('등급은 C')
#     else:
#         print('등급은 F')
# average = grade('홍길동', 20, 국어=90,영어=89,수학=77)
# average = grade('홍길동', number=20, 국어=90,영어=89,수학=77)

# #만약 grade 함수가 grade(name, number=1, *points)로 변경된 경우에 함수 실행문을 재 작성하면?
# def grade(name,*points, number=1):
#     avg = sum(points)/len(points)
#     print(f'{name}은 학번 {number}이며 평균은 {avg:.2f}')
#     return avg
# if __name__ == "__main__":
#     average = grade('홍길동', 90, 89, 77)
#     if average >= 90:
#         print('등급은 A')
#     elif average >= 80:
#         print('등급은 B')
#     elif average >= 70:
#         print('등급은 C')
#     else:
#         print('등급은 F')
# average = grade('홍길동', 20, 90, 89, 77)
# average = grade('홍길동', 90, 89, 77, number=20)   #TypeError: grade() got multiple values for argument 'number'   -> grade(name, *points, number=1) 순서로 함수 실행문 바꿔줘야??