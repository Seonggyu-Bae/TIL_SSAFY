import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
B. 데이터 전처리 : 2021년 이후의 종가 데이터 출력하기
• csv 파일을 DataFrame 으로 읽어와 2021년 이후의 데이터만 필터링합니다.
• [힌트] 필터링이 가능한 형식으로 데이터 타입을 변경한 후 필터링을 진행합니다.
• Pandas 의 to_datetime() 을 활용합니다.
• 필터링이 완료된 DataFrame 의 종가 데이터를 Matplotlib 를 사용하여 시각화 합니다.
"""

csv_path = "data/NFLX.csv"
arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)



df["Date"] = pd.to_datetime(df["Date"])
after2021_df = df[df["Date"] >= "2021-01-01"]

plt.plot(after2021_df['Date'], after2021_df['Close'])
plt.legend()
plt.title('NFLX Close Prices after 2021')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.show()