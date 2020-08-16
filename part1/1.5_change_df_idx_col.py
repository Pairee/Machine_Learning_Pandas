import pandas as pd

# 행 인덱스/열 이름 지정하여 데이터 프레임 만들기

df= pd.DataFrame(data=[[15,'남','덕영중'],[17,'여','수리중']],
                index=['준서','재민'],
                columns=['나이','성별','학교'])

# 행 인덱스, 열 이름 확인하기
print(df)
print('\n')

print(df.index)
print('\n')
print(df.columns)

# 행 인덱스, 열 이름 변경하기
df.index = ['학생1','학생2']
df.columns = ['연령','남녀','소속']

print(df)
print('\n')
print(df.index)
print(df.columns)
