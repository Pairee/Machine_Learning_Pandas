import pandas as pd

# DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
exam_data = {'수학': [10, 20, 30],
             '영어': [20, 30, 40],
             '체육': [30, 40, 50],
             '음악': [11, 12, 13]}

df = pd.DataFrame(data= exam_data, index=['서준','우현','예은'])
print(df)
print('\n')

# 데이터프레임 df를 복제하여 변수 df4에 저장 df4의 1개 열(column) 삭제
df4 = df[:]
df4.drop('수학',axis=1, inplace=True)

print(df4)
print('\n')

# 데이터프레임 df를 복제하여 변수 df5에 저장 df5의 2개 열(columns) 삭제
df5 = df[:]
df5.drop(['수학','영어'], axis = 1,inplace=True)

print(df5)