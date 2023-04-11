#1
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', options = specific_options)


URL = "https://www.waternow.go.kr/web/ssdoData/?pMENUID=8&ATTR_1=2020&ATTR_5=5"

driver.get(URL)

year = int(input())
rank = int(input())

yearBox = driver.find_element(By.NAME, 'selectYear')
yearBox.send_keys(year)
time.sleep(1)

Btn = driver.find_element(By.CLASS_NAME, 'btn01')
Btn.click()
time.sleep(1)


soup = BeautifulSoup(driver.page_source, 'html.parser')


table = soup.find('table', class_ = 'table01num')
trs = table.find_all('tr')
trs = trs[3:]
L = []

for tr in trs:
    tds = tr.find_all('td')
    data = tds[4].text
    data = data.strip()
    L.append(data)

for i in range(18):
    if ',' in L[i]:
        idx = L[i].find(',')
        L[i] = L[i][:idx] + L[i][idx + 1:]
    L[i] = int(float(L[i]))

L.sort()
print(L)
print(L[-rank])
















# #2
import pandas as pd

info = pd.read_csv("C:/Users/노채린/OneDrive/Documents/2022-2 강의/컴퓨터프로그래밍II/기출문제/답안_자료_TestCases/프로그래밍_자료/info.csv")
print(type(list(info['GENDER'])))

# df = info.drop('ID', axis = 1)

G = list(df['GENDER'])
A = list(df['AGE'])
M = list(df['MEMBER'])

L = []
for i in range(len(df)):
    L.append(G[i] + A[i] + M[i])

S = list(set(L))

result = [0] * len(S)
for i in range(len(L)):
    for j in range(len(S)):
        if L[i] == S[j]:
            result[j] += 1

k = int(input())
count = 0
for n in result:
    if n > 1:
        count += 1

if count >= k:
    print("YES")
else:
    print("NO")






#3
class Player:
    team = 'TIGERS'

    def __init__(self, avg, hr, age):
        self.avg = avg
        self.hr = hr
        self.age = age

    def sum_player(self, another):
        print(self.hr + another.hr)

bh = Player(0.378,15,33)
sb = Player(0.359,12,25)
dh = Player(0.315,17,29)

# sb.sum_player(dh)
