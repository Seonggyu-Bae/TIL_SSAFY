import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
E. 데이터 시각화 – 2022년 이후 최고, 최저, 종가 시각화하기
• csv 파일을 DataFrame 으로 읽어와 2022년 이후의 데이터만 필터링합니다.
• Matplotlib 를 활용하여 3가지 필드를 한 번에 분석할 수 있도록 아래와 같이 시각화 합니다.

"""

csv_path = "data/NFLX.csv"

arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)

#2022년 이후의 데이터만 필터링
df["Date"] = pd.to_datetime(df["Date"])
after2022_df = df[df["Date"] >= "2022-01-01"]

#Matplotlib 를 활용하여 3가지필드(고가,저가,종가)를 한번에 분석
plt.plot(after2022_df['Date'], after2022_df['High'])
plt.plot(after2022_df['Date'], after2022_df['Low'])
plt.plot(after2022_df['Date'], after2022_df['Close'])
plt.legend()
plt.title('High, Low and Close Prices since Jan 2022')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()
