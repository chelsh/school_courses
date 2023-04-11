import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', options = specific_options)

URL = ""



driver.get(URL)

soup = BeautifulSoup(driver.page_source, 'html.parser')




page = requests(URL)
page = page.text
soup = BeautifulSoup(page, 'html.parser')

# KMeans (K-평균 군집화)__________________________________________________________________________________________________

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

plt.figure(figsize=(10,5))

df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/menu.csv")


df_data = df[['가격', '판매량']]
km = KMeans(n_clusters = 4, random_state = 0)
result = km.fit_predict(df_data)

print(km.cluster_centers_)
df['Result'] = result

plt.scatter(df['가격'], df['판매량'], c = result)

plt.show()


# 밀도 기반 군집화 - DBSCAN ________________________________________________________________________________________________

import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

plt.figure(figsize = (10, 5))

df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/housing.csv")
df_data = df[['x', 'y']]

db = DBSCAN(eps = 10, min_samples = 3)
result = db.fit_predict(db)

df['Result'] = result

plt.scatter(df_data['x'], df_data['y'], c = result)

plt.show()


# 계층적 군집화 ________________________________________________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

plt.figure(figsize = (10, 5))

df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/housing.csv")
df_data = df[['x', 'y']]

linked = linkage(df_data, 'single')
dendrogram(linked, orientation = 'top')

plt.show()


"C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/exam/screenshot/.png"