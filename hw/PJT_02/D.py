import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
D. 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기
• csv 파일을 DataFrame 으로 읽어와 2021년 이후의 데이터만 필터링합니다.
• 월 별로 그룹화하여 평균 종가를 계산한 새로운 DataFrame 을 만들어 그래프로 시각화 합니다.
"""

csv_path = "data/NFLX.csv"
arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)


df["Date"] = pd.to_datetime(df["Date"])
after2021_df = df[df["Date"] >= "2021-01-01"]


new_df = after2021_df.groupby(pd.Grouper(key='Date', axis = 0 , freq='M')).mean()
plt.plot(new_df.index, new_df['Close'])
plt.legend()
plt.title('Monthly Average Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation = 0)
plt.show()