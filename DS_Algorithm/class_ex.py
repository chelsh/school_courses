class Monster:
    def __init__(self, img, hp, dmg, exp):
        self.img = img
        self.hp = hp
        self.dmg = dmg
        self.x = 180
        self.exp = exp
    
    def attack(self, user):
        user.hp -= self.dmg
    
    def attacked(self, user):
        self.hp -= user.dmg
    


class User:
    pass

lyn = User()
slime = Monster("slime.png", 100, 20, 30)





class Person:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def bmi(self):
        return self.w/(self.h**2)
    
    def testscore():
        pass

people = [Person(1.81, 78), Person(1.61,48)]

people[0].h = 1.6

for pers in people:
    print(pers.bmi())

    Person.bmi(pers)
    pers.bmi()
    print(pers.h)

