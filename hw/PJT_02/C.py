import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
C. 데이터 분석 : 2021년 이후 최고, 최저 종가 출력하기
• csv 파일을 DataFrame 으로 읽어와 2021년 이후의 데이터만 필터링합니다.
• 종가(Close) 필드를 활용하여, 2021년 이후 가장 높은 종가와 가장 낮은 종가를 출력합니다.
• Pandas 의 내장 함수를 사용합니다.
"""

csv_path = "data/NFLX.csv"
arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)



df["Date"] = pd.to_datetime(df["Date"])
after2021_df = df[df["Date"] >= "2021-01-01"]


close_max = after2021_df['Close'].max()
close_min = after2021_df['Close'].min()
print('최고 종가:',close_max)
print('최저 종가:',close_min)