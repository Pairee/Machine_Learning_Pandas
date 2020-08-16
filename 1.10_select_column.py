import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장

exam_data = {
    '이름':['서준','우현','인아'],
    '수학':[1,2,3],
    '영어':[4,5,6],
    '과학':[11,23,12],
    '체육':[12,55,23]
}

df = pd.DataFrame(exam_data)

print(df)
print(type(df))

# '수학' 점수 데이터만 선택, 변수 math1에 저장
math1 = df["수학"]
print(math1)
print(type(math1))

# '영어' 점수 데이터만 선택. 변수 english에 저장
english = df.영어
print(english)
print(type(english))

# '과학','체육' 점수 데이터 선택 시 변수 sci_gym에 저장
sci_gym = df[['과학','체육']]
print(sci_gym)
print(type(sci_gym))

# '수학' 점수 데이터만 선택. 변수 math2에 저장
math2 = df[["수학"]]
print(math2)
print(type(math2))
