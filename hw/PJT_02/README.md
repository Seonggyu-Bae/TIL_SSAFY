# 관통프로젝트 2

---

첫번째 프로젝트보다는 좀 수월하게 한 것 같다.

파이썬에 좀 익숙해진것도 있고 첫번째 프로젝트를 하면서 이것저것 배운게 많아서 그런것 같다.



데이터 처리 할때 파이썬이 좋다는 소리는 많이 들었지만 실제로 사용해보니 더 체감이 된다.

이게 있나 싶어서 찾아보면 여러 도구들이 나오고 사용방법이 나오는 신기한 언어인 것 같다.



파이썬과 Pandas 를 사용한 데이터 처리를 배웠고 크게 4가지를 배웠다

1. 데이터를 읽어 오는 것

2. 데이터를 필터링 가능한 형식으로 데이터 타입을 변환하는 법

3. 데이터를 내가 원하는 범위로 처리하는 것(전처리)

4. 데이터 분석

5. 데이터 시각화



그 중 월 별로 그룹화 하여 평균 종가를 계산한 새로운 DataFrame을 만드는 작업이 가장 까다로웠다.

아무래도 다른 것들은 사용법이 간단하고 직관적이라 쉽게 문제를 해결할 수있었는데

그룹화 하는건 처음 써봐서 좀 어려웠다. 



이전 회사에서 엑셀의 vlookup으로 노가다를 한 적이 있었는데 그때 파이썬을 알았다면 쉽게 해결 할 수있었을 것 같다는 생각이 든다.




---



### A. 데이터 전처리 : 데이터 읽어오기

1. csv파일의 ['Date', 'Open','High','Low','Close'] 필드만 읽어오도록 arr를 선언함

2. arr를 DataFrame으로 변환

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "data/NFLX.csv"
arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)
print(df)
```

---

### B. 데이터 전처리 : 2021년 이후의 종가 데이터 출력하기

1. A를 그대로 가져오고

2. 2021년 이후의 데이터만 필터링
   
   1. **to.datetime() 으로 필터링이 가능한 형식으로 데이터 타입 변경 필요**

3. 필터링이 완료된  DataFrame의 종가 데이터를 Matplotlib을 사용하여 시각화

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


csv_path = "data/NFLX.csv"
arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)

# 2021년 이후의 데이터만 필터링
df["Date"] = pd.to_datetime(df["Date"])
after2021_df = df[df["Date"] >= "2021-01-01"]

plt.plot(after2021_df['Date'], after2021_df['Close'])
plt.legend()
plt.title('NFLX Close Prices after 2021')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.show()
```

---

### C. 데이터 분석 : 2021년 이후 최고, 최저 종가 출력하기

1. A, B의 전처리 과정을 거친 후

2. DataFrame의 종가(Close) 필드를 활용하여 2021년 이후 가장 높은 종가와 가장 낮은 종가를 출력

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


csv_path = "data/NFLX.csv"
arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)



df["Date"] = pd.to_datetime(df["Date"])
after2021_df = df[df["Date"] >= "2021-01-01"]


close_max = after2021_df['Close'].max()
close_min = after2021_df['Close'].min()
print('최고 종가:',close_max)
print('최저 종가:',close_min)
```

---

### D. 데이터 분석 : 2021년 이후 월 별 평균 종가 출력하기

1. A,B 의 전처리 과정을 수행
2. 월 별로 그룹화하여 평균 종가를 계산한 새로운 DataFrame 을 만들어 그래프로 시각화 



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


csv_path = "data/NFLX.csv"
arr = pd.read_csv(csv_path, encoding = 'cp949', usecols = ['Date', 'Open','High','Low','Close'] )
df = pd.DataFrame(arr)


df["Date"] = pd.to_datetime(df["Date"])
after2021_df = df[df["Date"] >= "2021-01-01"]

#월 별로 그룹화하여 평균 종가를 계산한 새로운 DataFrame 을 만듬
new_df = after2021_df.groupby(pd.Grouper(key='Date', axis = 0 , freq='M')).mean()

#그래프로 시각
plt.plot(new_df.index, new_df['Close'])
plt.legend()
plt.title('Monthly Average Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation = 0)
plt.show()
```





---



### E. 데이터 시각화 : 2022년 이후 최고, 최저, 종가 시각화하기

1. csv 파일을 DataFrame 으로 읽어와 2022년 이후의 데이터만 필터링합니다.

2. Matplotlib 를 활용하여 3가지 필드(고가, 저가, 종가)를 한 번에 분석



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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


```
