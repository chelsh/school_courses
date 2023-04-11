#5 (3)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/노채린/source/repos/workspace/CPII/job.xlsx")

cond_2017 = df['기간'] == 2017
df_new = df.loc[cond_2017]
df_new = df_new.iloc[1:, :]

plt.figure(figsize = (10, 5))

df_new.plot(kind = 'scatter', x = '졸업자 수', y = '취업자 수')

plt.title("2017년 구 별 특성화고 졸업자 수와 취업자 수 산점도")
plt.xlabel("졸업자 수")
plt.ylabel("취업자 수")

plt.show()

