import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장

exam_data = {
    '이름': ['서준','우현','인아'],
    '수학': [50,20,30],
    '영어': [80,82,89],
    '음악': [70,72,79],
    '체육': [50,52,59]
}

df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경 사항 반영
df.set_index('이름', inplace= True)
print(df)

# 데이터프레임 df의 특정 원소 1개 선택('서준'의 '음악' 점수)
a = df.loc['서준','음악']
#a = df.loc[['서준','우현']] 서준 우현 행 선택 !
print(a)
b = df.iloc[0,2]
print(b)

# 데이터프레임 df의 특정 원소 2개 이상 선택 '서준'의 '음악', '체육' 점수
c = df.loc['서준',['음악','체육']]
print(c)
d = df.iloc[0,[2,3]]
print(d)
e  = df.loc['서준','음악':'체육']
print(e)
f = df. iloc[0,2:]

# df 2개 이상의 행과 열에 속하는 원소들 선택('서준'. '우현'의 '음악',체육' 점수)

g = df.loc[['서준','우현'],['음악','체육']]
print(g)
h = df.iloc[[0,1],[2,3]]
print(h)
i = df.loc['서준':'우현','음악':'체육']
print(i)
j = df.iloc[0:2,2:]
