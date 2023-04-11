import requests
from bs4 import BeautifulSoup


url = 'https://www.genie.co.kr/chart/top200'

header_info = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

page = requests.get(url, headers=header_info)
page = page.text

print(page)

soup = BeautifulSoup(page, 'html.parser')

top50_songs = soup.find_all('a', class_ = 'title ellipsis')

top50_list = []

for song in top50_songs:
    songName = song.text
    songName = songName.strip()
    top50_list.append(songName)

print(top50_list)
print(len(top50_list))






#Exercise 1
import requests
from bs4 import BeautifulSoup

url = "https://info.korea.ac.kr/info/community/circle.do"
headers_info = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

page = requests.get(url, headers=headers_info)
page = page.text

soup = BeautifulSoup(page, 'html.parser')

clubs = soup.find_all('h4', class_ =  'h4-tit01')

club_list = []

for club in clubs:
    c = club.text
    c = c.strip()
    club_list.append(c)

print(club_list)            #['ALPS', 'CAT&DOG', 'KOSMOS', 'KUICS', 'LIBERTY', 'FLIPFLOP', '소아달', '전산학술부', 'KWEB']









#Exercise 2 
import requests
from bs4 import BeautifulSoup

url = "https://www.kovo.co.kr/stats/41200_mvp.asp?s_part=2"
header_info = {"User-Agent":"/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

page = requests.get(url, headers = header_info)
page = page.text

soup = BeautifulSoup(page, 'html.parser')

mvps = soup.find_all('td', class_ = "border_left")

mvp_list = []
for mvp in mvps:
    m = mvp.text
    m = m.strip()
    mvp_list.append(m)

mvp_list = [mvp_list[i] for i in range(len(mvp_list)) if i % 3 == 2]

mvp_set = set(mvp_list)
mvp_dict = dict()

for i in mvp_set:
    mvp_dict[i] = 0

for i in mvp_list:
    mvp_dict[i] += 1

mostMVPs = [k for k, v in mvp_dict.items() if max(mvp_dict.values()) == v]

for mostMVP in mostMVPs:
    print(mostMVP)







#Selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', options = specific_options)

driver.get("https://portal.korea.ac.kr/front/Intro.kpd")
time.sleep(1)
driver.save_screenshot('C:/Users/노채린/source/repos/workspace/CPII/screenshot/beforeLogin.png')



id_box = driver.find_element(By.NAME, 'id')
pw_box = driver.find_element(By.NAME, 'pw')

id_box.send_keys("sinye2002")
pw_box.send_keys("cofls0425*")

driver.save_screenshot("C:/Users/노채린/source/repos/workspace/CPII/screenshot/after_send_id&pw.png")

login_button_xpath = "//*[@id=\"loginsubmit\"]"
login_button = driver.find_element(By.XPATH, login_button_xpath)
login_button.click()

time.sleep(2)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/CPII/screenshot/after_login.png")

soup = BeautifulSoup(driver.page_source, 'html.parser')








#Exercise 3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

option_list = ['--headless', '--no-sandbox']
specific_options = webdriver.ChromeOptions()
for op in option_list:
    specific_options.add_argument(op)

driver = webdriver.Chrome('chromedriver', options = specific_options)




url = "https://likms.assembly.go.kr/record/mhs-60-010.do"
driver.get(url)


conference_div = driver.find_element(By.NAME, "CLASS_CODE")
conference_div.send_keys("국회본회의")
time.sleep(1)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/CPII/screenshot/국회본회의.png")

srchButton = driver.find_element(By.ID, "srchBtn")
srchButton.click()
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/CPII/screenshot/국회본회의 검색 클릭.png")

pdfBtn = driver.find_element(By.XPATH, "//*[@id=\"srchResultUl\"]/li[1]/div[2]/div/a[2]/img")
pdfBtn.click()
