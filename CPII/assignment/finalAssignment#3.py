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
