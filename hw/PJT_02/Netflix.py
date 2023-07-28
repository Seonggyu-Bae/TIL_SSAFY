import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "data/NFLX.csv"

"""
A. 데이터 전처리 -데이터 읽어오기
Pandas를 사용하여 csv파일을 DataFrame으로 읽어옴
['Date', 'Open','High','Low','Close'] 필드만 읽어오도록 arr를 선언함
"""

arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)
print(df)




"""
B. 데이터 전처리 : 2021년 이후의 종가 데이터 출력하기
• csv 파일을 DataFrame 으로 읽어와 2021년 이후의 데이터만 필터링합니다.
• [힌트] 필터링이 가능한 형식으로 데이터 타입을 변경한 후 필터링을 진행합니다.
• Pandas 의 to_datetime() 을 활용합니다.
• 필터링이 완료된 DataFrame 의 종가 데이터를 Matplotlib 를 사용하여 시각화 합니다.
"""


df["Date"] = pd.to_datetime(df["Date"])
after2021_df = df[df["Date"] >= "2021-01-01"]

plt.plot(after2021_df['Date'], after2021_df['Close'])
plt.legend()
plt.title('NFLX Close Prices after 2021')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.show()


"""
C. 데이터 분석 : 2021년 이후 최고, 최저 종가 출력하기
• csv 파일을 DataFrame 으로 읽어와 2021년 이후의 데이터만 필터링합니다.
• 종가(Close) 필드를 활용하여, 2021년 이후 가장 높은 종가와 가장 낮은 종가를 출력합니다.
• Pandas 의 내장 함수를 사용합니다.
"""
close_max = after2021_df['Close'].max()
close_min = after2021_df['Close'].min()
print('최고 종가:',close_max)
print('최저 종가:',close_min)



"""
D. 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기
• csv 파일을 DataFrame 으로 읽어와 2021년 이후의 데이터만 필터링합니다.
• 월 별로 그룹화하여 평균 종가를 계산한 새로운 DataFrame 을 만들어 그래프로 시각화 합니다.

"""

new_df = after2021_df.groupby(pd.Grouper(key='Date', axis = 0 , freq='M')).mean()

plt.plot(new_df.index, new_df['Close'])
plt.legend()
plt.title('Monthly Average Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.show()


"""
E. 데이터 시각화 – 2022년 이후 최고, 최저, 종가 시각화하기
• csv 파일을 DataFrame 으로 읽어와 2022년 이후의 데이터만 필터링합니다.
• Matplotlib 를 활용하여 3가지 필드를 한 번에 분석할 수 있도록 아래와 같이 시각화 합니다.

"""
after2022_df = df[df["Date"] >= "2022-01-01"]

plt.plot(after2022_df['Date'], after2022_df['High'])
plt.plot(after2022_df['Date'], after2022_df['Low'])
plt.plot(after2022_df['Date'], after2022_df['Close'])
plt.legend()

plt.title('High, Low and Close Prices since Jan 2022')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()

