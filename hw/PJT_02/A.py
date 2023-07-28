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
