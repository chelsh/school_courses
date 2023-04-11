#1
def eleven(a, b, c, d):
    result = [a] * 8

    for i in range(4):
        result[i] += b
    
    for i in range(4,8):
        result[i] -= b

    result[0] += c
    result[1] += c
    result[4] += c
    result[5] += c

    result[2] -= c
    result[3] -= c
    result[6] -= c
    result[7] -= c

    for i in range(8):
        if i % 2 == 0:
            result[i] += d
        else:
            result[i] -= d

    if 11 in result:
        return True
    else:
        return False





#2
import requests
from bs4 import BeautifulSoup


URL = "https://www.kamis.or.kr/customer/price/product/period.do?action=monthly"
page = requests.get(URL)
page = page.text

soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table', id = 'itemTable_102')
trs = table.find_all('tr')
trs = trs[1:]


tds = []
for tr in trs:
    td = tr.find_all('td')
    L = []
    for t in td:
        d = t.text
        d = d.strip()
        L.append(d)
    tds.append(L)


year = int(input())
month = int(input())

Y = tds[year - 2019]

result = Y[month]
idx = result.find(',')

result = result[:idx] + result[idx + 1:]

print(result)








#3
import pandas as pd

df = pd.read_csv("C:/Users/노채린/OneDrive/Documents/2022-2 강의/컴퓨터프로그래밍II/기출문제/답안_자료_TestCases/프로그래밍_자료/bicycle.csv")

df = df[['자전거대여소명','자전거보유대수']]

n = int(input())

cond = df['자전거보유대수'] >= n

df = df[cond]
print(df['자전거보유대수'].count())