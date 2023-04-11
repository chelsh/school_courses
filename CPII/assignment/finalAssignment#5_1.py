#5 (1)
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family = 'NanumBarunGothic')

df = pd.read_excel("C:/Users/노채린/source/repos/workspace/CPII/job.xlsx", index_col = 0)

cond_nowon = df["자치구"] == "노원구"
df_nowon = df.loc[cond_nowon]
df_nowon_work = df_nowon.loc[:, "취업률"]

plt.figure(figsize = (10, 5))

df_nowon_work.plot()

plt.title("노원구 특성화고 8년간 취업률 변화")
plt.xlabel("연도")
plt.ylabel("취업률")

plt.show()

