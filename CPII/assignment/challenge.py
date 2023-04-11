import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://info.nec.go.kr/main/showDocument.xhtml?electionId=0000000000&topMenuId=EP&secondMenuId=EPEI01"

specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', options = specific_options)

driver.get(url=URL)

lawmaker = driver.find_element(By.ID, "electionType2")      # 선거유형 > 국회의원선거 클릭
lawmaker.click()

electionName = driver.find_element(By.NAME, "electionName")     # 조회조건 > 제21대 선택
electionName.send_keys("제21대")
time.sleep(1)

electionCode = driver.find_element(By.NAME, "electionCode")     # 조회조건 > 선거 > 국회의원선거 선택
electionCode.send_keys("국회의원선거")
time.sleep(1)


districts = input().split()     # 광역자치단체 띄어쓰기로 구분해서 입력

for dt in districts:
    cityCode = driver.find_element(By.NAME, "cityCode")     # 조회조건 > 시도

    cityCode.send_keys(dt)   # 입력받은 광역자치단체 넣기
    time.sleep(1)

    srchBtn = driver.find_element(By.XPATH, "//*[@id=\"searchBtn\"]")   # 검색 버튼
    srchBtn.click()
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')     # selenium으로 웹페이지의 html소스 가져와서 Beautifulsoup으로 파싱

    tr = soup.find_all('tr')
    
    df_dict = dict()        # dict로 dataframe 생성 

    districtNames = []
    partyNames = []
    pollingRatio = []

    for i in range(1, len(tr)):
        data = tr[i].find_all('td')

        ptName =  data[1].text.strip()

        if ptName != '무소속':      # 정당명 != '무소속'인 경우만 반영

            dtName = data[0].text.strip()
            Ratio = data[-1].text.strip()
            
            stIdx = Ratio.find('(')
            endIdx = Ratio.find(')')
            Ratio = float(Ratio[stIdx + 1:endIdx])

            districtNames.append(dtName)
            partyNames.append(ptName)
            pollingRatio.append(Ratio)
    
    df_dict['선거구명'] = districtNames
    df_dict['정당명'] = partyNames
    df_dict['득표율'] = pollingRatio

    df = pd.DataFrame(df_dict)
    df = df.set_index(keys = '선거구명')
    df = df.sort_values(by = '득표율')      # 득표율 기준 정렬

    gap = []                                # 득표율 차의 절대값 저장
    for i in range(len(df) - 1):
        gap.append(abs(df.iloc[i,1] - df.iloc[i+1,1]))      
    
    end_flag = 1
    while end_flag:
        minIdx = gap.index(min(gap))

        if df.iloc[minIdx, 0] != df.iloc[minIdx + 1, 0]:        # 소속 정당이 서로 다른 경우에 출력
            print(df.index[minIdx], df.index[minIdx + 1])
            end_flag = 0

        else:                                                   # 정당이 같은 경우 제외 
            gap[minIdx] = 100