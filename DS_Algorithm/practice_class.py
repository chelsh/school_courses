# class Univ:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#     def entrance(self):
#         self.ent_year = self.number[:4]
#     def graduation(self, year):
#         pass

# class College(Univ):
#     def __init__(self, name, number, department):
#         super().__init__(name,number)
#         self.department = department
#     def graduation(self, year):
#         self.entrance()
#         print(f"졸업까지 총 {year - int(self.ent_year)}년 걸렸음")

#     def __repr__(self):
#         return f"{self.name}은 {self.department}입니다."

# if __name__=="__main__":
#     student1 = College("Lyn", "20211302", "kh")
#     student1.graduation(2022)
#     print(student1)


# from dataclasses import dataclass


# @dataclass
# class Person:
#     name: str
#     sex: str
#     age: int
#     __alive: bool = True

#     def sayHello(self):
#         print("Hi, I'm", self.name)

#     def __exist(self):
#         return True   

# p1 = Person("Lini", 'F', 21, False)
# print(p1)
# # print(p1.__alive)
# p1.sayHello()


# s = [] # or s = list()
# for i in range(2):
#     temp = input().split()
#     s.append(temp)
# print(s)
# for data in s:
#     print(f'{data[0]}: {data[1]} & {data[2]}')

# mydict = {'a' : 1, 'b' : 2}
# print(mydict['a'])



from collections import namedtuple

Profile = namedtuple(typename='Profile',field_names=['name','age','city','phone'])
#namedtuple('Profile','name, age, city, phone')
temp = Profile("유나",21, "인천시","0105558888")
print(temp[0])
print(temp.name)

profile = [('gildong', 20, '서울시','0105555555'),
('young', 22, '부산시','0105557777'),]
print(profile[0][0])

profile_ = [Profile(p[0],p[1],p[2],p[3]) for p in profile]
info = [Profile._make(p) for p in profile]
print(profile_[0].name)
print(profile_[0]._asdict())