import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram


df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/menu.csv")

df_data = df.loc[:, ['가격', '판매량']]
km = KMeans(n_clusters = 4, random_state = 0)
km.fit(df_data)
result = km.predict(df_data)

print(km.cluster_centers_)
df.loc[:, 'result'] = result

print(df)

plt.figure(figsize = (10, 5))

# df.plot(kind = 'scatter', x = '가격', y = '판매량', c = result)
plt.scatter(df.loc[:,'가격'], df.loc[:,'판매량'], c = result)

plt.show()






#Exercise 1

#(1)
df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/broadcast.csv")

df_data = df.drop('프로그램명', axis = 1)
km = KMeans(n_clusters = 3, random_state = 0)
km.fit(df_data)
result = km.predict(df_data)

plt.figure(figsize = (10, 5))

plt.scatter(df_data.loc[:, '시청률'], df_data.loc[:, '시청연령'], c = result)

# plt.show()

#(2)
df.loc[:, 'result'] = result
# print(df)     # 뮤뱅, 음중 같은 그룹 배정됨





df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/housing.csv")
house_position = df[['x', 'y']]

db = DBSCAN(eps = 10, min_samples = 3)
cluster_pred = db.fit_predict(house_position)

df['result'] = cluster_pred

plt.figure(figsize=(10,5))

x = house_position['x']
y = house_position['y']
plt.scatter(x, y, c = cluster_pred)

plt.show()






#Exercise 2
df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/climate.csv")









df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/housing.csv")
house_position = df[['x', 'y']]

linked = linkage(house_position, 'single')
dendrogram(linked, orientation='top')

plt.figure(figsize=(10,5))

plt.show()






#Exercise 3
df = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/student.csv")

# total = df['KoreanScore'] + df['MathScore'] + df['EnglishScore']
# df['TotalScore'] = total
# print(df)

data = df[['KoreanScore', 'MathScore']]
linked = linkage(data, 'single')
dendrogram(linked, orientation = 'top')

plt.figure(figsize=(10,5))
plt.show()