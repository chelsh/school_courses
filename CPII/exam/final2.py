import pandas as pd

df = pd.read_csv('lecture.csv')
df = df.drop('date', axis = 1)

L = list(df['name'])
S = list(set(L))
D = dict()
for name in S:
    D[name] = 0

for i in range(len(df)):
    score = 0
    if df.loc[i,'part'] == 'HW':
        if df.loc[i,'grade'] == 'Pass':
            score += 20
    elif df.loc[i,'part'] == 'Mid':
        score += int(df.loc[i,'grade'])
    elif df.loc[i,'part'] == 'Final':
        score += int(df.loc[i,'grade'])
   
    D[df.loc[i, 'name']] += score

V = [k for k in D.values()]
V.sort()
V.reverse()
student = input()

s = D[student]
i = V.index(s)
print(i + 1)