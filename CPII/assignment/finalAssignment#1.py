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
