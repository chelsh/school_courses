#Exercise 1,2,3
class City:
    country: "대한민국"
    
    def __init__(self, name, do, population, area):
        self.name = name
        self.do = do
        self.population = population
        self.area = area

    def city_info(self):
        if self.population >= 1_000_000:
            return self.do + " " + self.name + "특례시"
        elif self.population >= 50_000:
            return self.do + " " + self.name + "시"
        else:
            return self.do + " " + self.name + "군"

    def city_unite(self, city):
        print(f'''도시간 흡수 통합을 실시합니다.
통합 대상 지역 : {self.city_info()}
흡수 대상 지역 : {city.city_info()}
통합 결과 인구수 : {str(self.population + city.population)} 명
통합 결과 면적 : {str(self.area + city.area)} km^2''')
        self.population += city.population
        self.area += city.area
        del city

    def __del__(self):
        print(self.name, "소멸")


yongIn = City("용인", "경기도", 1092315, 591.3)
chungJu = City("충주", "충청북도", 210186, 984.0)
boEun = City("보은", "충청북도", 31812, 584.3)


print(yongIn.city_info())
print(chungJu.city_info())
print(boEun.city_info())

chungJu.city_unite(boEun)
print(yongIn.city_info())
print(chungJu.city_info())
print(boEun.city_info())

while True:
    pass