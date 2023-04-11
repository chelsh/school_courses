#4
import pandas as pd

TOTAL_SCORE = 'TotalScore'

df = pd.read_csv("C:/Users/노채린/source/repos/workspace/CPII/score.csv", index_col = 0)


low = df[TOTAL_SCORE].quantile(0.25)
high = df[TOTAL_SCORE].quantile(0.75)

IQR = high - low

superior = df.loc[df[TOTAL_SCORE] >= high + IQR]
inferior = df.loc[df[TOTAL_SCORE] <= low - IQR]


for i in superior.index:
    print(i, "학생 대단합니다!")

for i in superior.index:
    print(i, "학생 할 수 있어요!")

