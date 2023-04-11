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
