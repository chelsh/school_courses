from bs4 import BeautifulSoup
import requests

book = input()

book = book.replace(' ', '+')

URL = "https://lib.seoul.go.kr/main/searchBrief?st=KWRD&si=TOTAL&lmt0=&sts=Y&searchType=&q=" + book

page = requests.get(URL)
page = page.text

soup = BeautifulSoup(page, 'html.parser')

btn = soup.find('span', class_ = 'availableBtn')
text = btn.text

if text == '신청가능':
    print("ASK")
elif text == '대출중':
    print("BUSY")
elif text == '대출가능':
    place = soup.find('p', class_ = 'location')
    t = place.text
    t = t.strip()
    L = t.split()
    stair = L[0]
    i = stair.find('(')
    j = stair.find('층')
    stair = stair[i + 1:j]
    print(stair)