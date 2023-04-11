#5 (2)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/노채린/source/repos/workspace/CPII/job.xlsx")

cond_2014 = df['기간'] == 2014
df_2014 = df.loc[cond_2014]

cond_region1 = df['자치구'] == '용산구'
cond_region2 = df['자치구'] == '서초구'
cond_region3 = df['자치구'] == '강남구'
df_new = df_2014.loc[cond_region1 | cond_region2 | cond_region3]

plt.figure(figsize = (10, 5))

df_new.plot(kind = 'bar', x = '자치구', y = '취업자 수')

plt.title("용산구-서초구-강남구 특성화고 취업자 수")

plt.show()

