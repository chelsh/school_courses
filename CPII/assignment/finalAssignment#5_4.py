#5 (4)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font', family = 'NanumBarunGothic')

df = pd.read_excel("C:/Users/노채린/source/repos/workspace/CPII/job.xlsx")

cond_2015 = df['기간'] == 2015
df_new = df.loc[cond_2015]
df_new = df_new.iloc[1:, :]

sns.lmplot(data = df_new, x = '졸업자 수', y = '취업자 수')

plt.title("2015년 구 별 특성화고 졸업자 수와 취업자 수 산점도")

plt.show()

 