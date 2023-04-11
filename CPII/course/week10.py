import pandas as pd


#Exercise 1

df = pd.read_excel("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/bike_info.xlsx", index_col = 0)

print(df)

print(df.loc[:,:])
print(df.iloc[:,:])

print('----------------------------')
print(df.iloc[0,0])




# Exercise 2

# dictionary로 생성
df_dict = dict()

df_dict['상호명'] = ['예예 치킨', '스타북스', '미세스 피자', '어디야 커피']
df_dict['시'] = ['서울특별시','서울특별시','서울특별시','서울특별시']
df_dict['구'] = ['관악구', '종로구', '중랑구', '은평구']
df_dict['동'] = ['대학동', '창신동', '면목동', '구파발동']

df1 = pd.DataFrame(df_dict)

df1 = pd.get_dummies(df1, columns=['시'])
print(df1)

#list로 생성
df_list = []
df_list.append(['예예 치킨', '서울특별시', '관악구', '대학동'])
df_list.append(['스타북스', '서울특별시', '종로구', '창신동'])
df_list.append(['미세스 피자', '서울특별시', '중랑구', '면목동'])
df_list.append(['어디야 커피', '서울특별시', '은평구', '구파발동'])

df2 = pd.DataFrame(df_list, columns= ['상호명', '시', '구', '동'])

df1 = df1.drop(0, axis=0)
df_new = pd.concat([df1,df2], axis=0)
df_new = df_new.reset_index(drop=True)
print(df_new.iloc[:,0])
print(df_new)

print(df1)
print(df2)


print(df1.iloc[[i for i in range(len(df1))], [0,1,2]])
print(df1.loc[[0, 2], ['시','구','동']])
print(df1.iloc[[2, 3], [0, 3]])


print(df2.iloc[[i for i in range(len(df2))], [0,1,2]])
print(df2.loc[[0, 2], ['시','구','동']])
print(df2.iloc[[2, 3], [0, 3]])


#Exercise 3
data = pd.read_csv("C:/Users/노채린/source/repos/workspace/2022_2_courses/CPII/data_sample/seodaemun.csv")


cond1 = data['동'] != '남가좌동'
cond2 = data['동'] != '북가좌동'

cond = cond1 & cond2
print(data[cond])