#1
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

option_list = ['--headless', '--no-sandbox']
specific_options = webdriver.ChromeOptions()
for op in option_list:
    specific_options.add_argument(op)

driver = webdriver.Chrome('chromedriver', options = specific_options)

url = "https://m.dhlottery.co.kr/gameResult.do?method=allWin"
driver.get(url)

N = input()

start = driver.find_element(By.NAME, "drwNoStart")
end = driver.find_element(By.NAME, "drwNoEnd")
start.send_keys(N)
end.send_keys(N)

srchBtn = driver.find_element(By.ID, "searchBtn")
srchBtn.click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
winnerNum = soup.find("td", class_ = "highlight")
winnerNum = winnerNum.text.split()

print(winnerNum[1])



#2
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

option_list = ['--headless', '--no-sandbox']
specific_options = webdriver.ChromeOptions()
for op in option_list:
    specific_options.add_argument(op)

driver = webdriver.Chrome('chromedriver', options = specific_options)

url = "https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=1_1&area=01"
driver.get(url)

y = input() + '년'
m = input() + '월'
d = input() + '일'
if len(m) == 2:
    m = '0' + m
if len(d) == 2:
    d = '0' + d

year = driver.find_element(By.NAME, 'sYear')
month = driver.find_element(By.NAME, 'sMonth')
date = driver.find_element(By.NAME, 'sDay')

year.send_keys(y)
month.send_keys(m)
date.send_keys(d)

srchBtn = driver.find_element(By.XPATH, '//*[@id="sub_body"]/table[1]/tbody/tr/td/form/table/tbody/tr/td[2]/img')
srchBtn.click()

soup = BeautifulSoup(driver.page_source, 'html.parser')

top20 = soup.find_all('td', class_ = "tb_txt")
top3 = []

for i in range(3):
    top = top20[i].text
    top3.append(top)

for top in top3:
    print(top[:-1])






#3
import requests
from bs4 import BeautifulSoup

year = input()
month = input()
date = input()
if len(month) == 1:
    month = '0' + month
if len(date) == 1:
    date = '0' + date


url = f"https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date={year}{month}{date}"

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

top1 = soup.find('div', class_ = 'tit5')
top1 = top1.text.strip()

print(top1)







#4
import pandas as pd
import math

TOTAL_SCORE = 'TotalScore'

df = pd.read_csv("C:/Users/노채린/source/repos/workspace/CPII/score.csv", index_col = 0)


low = df[TOTAL_SCORE].quantile(0.25)
high = df[TOTAL_SCORE].quantile(0.75)

IQR = high - low

superior = df.loc[df[TOTAL_SCORE] >= high + IQR]
inferior = df.loc[df[TOTAL_SCORE] <= low - IQR]


for i in superior.index:
    print(i, "학생 대단합니다!")

for i in superior.index:
    print(i, "할 수 있어요!")








# #5
# import pandas as pd