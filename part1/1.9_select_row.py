import pandas as pd

# DataFrame() 함수료 데이터프레임 변환. 변수 df에 저장

exam_data = {
    '수학': [1, 2, 3],
    '영어': [2, 4, 5],
    '체육': [4, 5, 5],
    '음악': [10, 20, 30]
}

df = pd.DataFrame(data=exam_data, index=['서준', '은아', '형철'])
print(df)
print('\n')

# 행 인덱스를 사용하여 행 1개 선택
label1 = df.loc['서준'] #loc 끝 범위 포함
position1 = df.iloc[0] #iloc 끝 범위 제외 

print(label1)
print(position1)

# 행 인덱스를 사용하여 2개 이상의 행 선택
label2 = df.loc[['서준','은아']]
position2 = df.iloc[[0,1]]
print(label2)
print(position2)

# 행 인덱스의 범위를 지정하여 행 선택
label3 = df.loc['서준':'은아']
position3 = df.iloc[0:2]
print(label3)
print(position3)
