# 23/07/18

#### Sequence Types : 여러 개의 값들을 <u>순서대로 나열</u>하여 저장하는 자료형

- Sequence Types 특징
  
  1. 순서(sequnece): 값들이 순서대로 저장(정렬 X)
  
  2. 인덱싱(Indexing): 각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수있음
  
  3. 슬라이싱(Slicing): 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
  
  4. 길이(Length): len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
  
  5. 반복(Iteration): 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음

##### 문자열 표현

- 문자열은 단일 문자나 여러 문자의 조합으로 이루어짐

- 작은따옴표 또는 큰따옴표로 감싸서 표현

- ```python
  #Hello, World!
  print('Hello, World!')
  
  #str
  print(type('Hello, World!'))
  ```

- **Escape sequence**
  
  - 역슬래시뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
  
  - 파이선의 일반적인 문법 규칙을 잠시 탈출한다는 의미

| 예약 문자 | 내용(의미) |
|:-----:|:------:|
| \n    | 줄 바꿈   |
| \t    | 탭      |
| \\\   | 백슬래시   |
| \'    | 작은 따옴표 |
| \"    | 큰 따옴표  |

- **f-string**
  
  - 문자열에 f 또는 F접두어를 붙이고 표현식을 {표현식}로 작성하여 문자열에 파이선 표현식의 값을 삽입가능
  
  - ```python
    bugs = 'roaches'
    counts = 13
    area = 'room'
    
    #Debugging roaches 13 room
    print(f'Debugging {bugs} {counts} {area}')
    ```

**문자열의 시퀀스 특징**

```python
my_str = 'hello'


print(my_str[1]) #e 인덱싱

print(my_str[2:4]) #ll 슬라이싱

print(len(my_str)) #5 길이
```



#### 인덱스(index)

- 시퀀스 내의 값들에 대한 고유한 번호로, 각 값의 위치를 식별하는데 사용되는 숫자



#### 슬라이싱(slicing)

- 시퀀스의 일부분을 선택하여 추출하는 작업

- 시작 인덱스와 끝 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스를 생성
  
  

#### 리스트(list)

- **여러 개의 값을 순서대로 저장하는 <u>변경 가능한</u> 시퀀스 자료형**

- 0개 이상의 객체를 포함하며 데이터 목록을 저장

- 대괄호로 표기

- 데이터는 어떤 자료형도 저장할 수있음

- ```python
  m_lst_1 = []
  m_lst_2 = [1, 'a', 3, 'b', 5]
  m_lst_3 = [1, 2, 3, 'python', ['hello', 'world', '!!!']]
  ```

- 리스트의 시퀀스 특징
  
  ```python
  m_lst = [1, 2, 3, 'python', ['hello', 'world', '!!!']]
  
  print(m_lst[1]) # 2
  
  print(m_lst[2:4]) #[3, 'python']
  print(m_lst[:3]) # [1, 2, 3,]
  print(m_lst[3:]) # ['python', ['hello', 'world', '!!!']]
  print(m_lst[0:5:2]) #[1, 3, ['hello', 'world', '!!!']]
  print(m_lst[[-1][1][0]) # w
  print(m_lst[::-1]) # [['hello', 'world', '!!!'], 'python', 3, 2, 1]
  ```
  
  

#### 튜플(tuple)

- **여러 개의 값을 순서대로 저장하는 <u>변경 불가능한 </u>시퀀스 자료형**

- 0개 이상의 객체를 포함하며 데이터 목록을 저장

- 소괄호로 표기

- 데이터는 어떤 자료형도 저장할 수 있음

```python
my_tuple = (1, 'a', 3, 'b, 5)



my_tuple[1] = 'z'
# TypeError : 'tuple object does not support item assignment'
```

- 튜플의 불변 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중할당 등 개발자가 직접 사용하기 보다 '파이선 내부 동작' 에서 주로 사용



#### range

- 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형

- range(n)
  
  - 0부터 n-1 까지의 숫자의 시퀀스

- range(n,m)
  
  - n부터 m-1까지의 숫자 시퀀스





## Non-sequence Types



#### 딕셔너리(dict)

- key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

- key는 변경 불가능한 자료형만 사용 가능

- value는 모든 자료형 사용 가능

- 중괄호로 표기

- ```python
  my_dict = {'apple': 12, 'list': [1, 2, 3]}
  
  print(my_dict['apple']) #12
  print(my_dict['list']) # [1, 2, 3]
  
  # change value
  my_dict
  ```



---

# 23/07/14

표현식(Expression)과 문장(statement)
문장은 보통 여러 개의 표현식을 포함함

- 문장은 실행 가능한 코드를

- 변수 : 값을 참조하는 이름 ( 프로그램이 실행되는 동안 값을 저장하는 장소임 )

- | 기호  | 연산자       |
  | --- | --------- |
  | -   | 음수 부호     |
  | +   | 더하기       |
  | -   | 뺄셈        |
  | *   | 곱셈        |
  | /   | 나눗셈       |
  | //  | 정수 나눗셈(몫) |
  | %   | 나머지       |
  | **  | 지수(거듭제곱)  |

Today

변수, 문자열, 리스트, 딕셔너리
출력,입력, 제어문, 반복문, 조건문

- 제어문(Control Statement)의 종류 : 반복문(for, while), 조건문(if)

#### 오늘 기본적인 문법을 배워서 파이선으로 가장 쉬운문제들을 풀어보았다.

### 홀수만 더하기

```python
T = int(input())

for test_case in range(1, T + 1):
    sum=0
    num_list = list(map(int, input().split()))

    for i in num_list:
        if i%2!=0:
            sum+=i

    print(f'#{test_case} {sum}')
```

### 최대수 구하기

```python
T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    max_num= max(num_list)
    print(f'#{test_case} {max_num}')
```

### 중간값 찾기

```python
T = int(input())

number = list(map(int, input().split()))
number.sort()

print(number[T//2])
```

### 자릿수 더하기

```python
number = list(map(int, input()))
sum_number = sum(number)
print(sum_number)
```

### 1대1 가위바위보

```python
a, b = map(int, input().split())

if (a - b == -2 or a - b == 1):
    print('A')
else:
    print('B')
```

### 최빈수 구하기

```python
T = int(input())

for test_case in range(1, T + 1):
    case_num = int(input())
    num_list = list(map(int, input().split()))
    num_count = [0] * 101

    for i in range(len(num_list)):
        num_count[num_list[i]] += 1

    max_num = 0
    max_index = 0
    # 최빈수가 여러개 일때는 가장 큰 점수 출력을 위해 >=
    for i in range(len(num_count)):
        if (num_count[i] >= max_num):
            max_num = num_count[i]
            max_index = i

    print(f'#{case_num} {max_index}')
```

### 23/07/13

---

### 1. 마크다운

- 일반 텍스트로 문서를 작성하는 간단한 방법

- 주로 개발자들이 텍스트와 코드를 작성해 문서화하기 위해 사용함

- 이 README도 마크다운으로 작성중

코드를 아래 처럼 문서화 할 수있다.

```python
print('Hello')
```

###### 문법을 굳이 외우지 않아도 마크다운 프로그램이 잘 되어 있어서 가져다 쓰면됨

사진, 링크도 넣을 수 있다 (이미지의 너비/높이는 마크다운으로 조절 **X** (HTML 문법 필요)

[네이버](https://www.naver.com/)

![아이유](https://img.tvreportcdn.de/cms-content/uploads/2023/07/12/e0d84f6c-e001-4acf-a949-226da0c3dd02.jpg)

출처 : [아이유, 데뷔 15주년 전시 '순간,'...오늘(12일) 일반 예매 티켓 오픈](https://tvreport.co.kr/breaking/article/742504/)

---

### 2. CLI

- Command Line Interface의 약자로 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식이다.

- 현재 우리가 보편적으로 사용하는 것은 GUI(Graphic User Interface)

![사진](https://postfiles.pstatic.net/MjAxOTEyMDFfNDYg/MDAxNTc1MTc3NTA3MzQ5.ZhJYxSKOH8XaObImS0BZjEwsTp58M_Th6R6OYK8zhlUg.8pzA2628XivwZPKN-611yKF_yGXTlTsCRvPlG02e5NEg.PNG.kyozoo72/image.png?type=w773)

출처 : [사람지능(Human Intelligence) : 네이버 블로그](https://blog.naver.com/human_intelligence/221723703567)

###### CLI 기초문법

- touch : 파일생성

- mkdir : 새 디렉토리(폴더) 생성

- ls : 현재 작업중인 디렉토리 내부의 폴더/파일 목록을 출력

- cd : 현재 작업 중인 디렉토리 위치를 변경

- start : 폴더/파일 열기 (Mac에서는 open)

- rm : 파일삭제(rm -r 으로 디렉토리 삭제가능)

###### CLI에서 가장 중요한것 : 내가 현재 작업 하고 있는 위치(경로)를 알아야함

- 절대 경로 : Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
  
  - 윈도우 바탕 화면까지의 절대 경로 예시 (C:/Users/ssafy/Desktop)

- 상대 경로 : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
  
  - 만약 현재 작업하고 있는 디렉토리가 C:/Users 일때, 윈도우 바탕화면으로의 상대 경로는 ssafy/Desktop

### 3. Git

###### 분산 버전 관리 시스템 : 코드의 '변경이력'을 기록하고 '협업'을 원활하게 하는 도구

- 버전관리란? : 변화를 기록하고 추적하는 것

###### git의 역할

- 코드의 버전(히스토리)를 관리

- 개발되어 온 과정 파악

- 이전 버전과의 변경 사항 비교\

###### Git의 3가지 영역

- Working Directory : 실제 작업 중인 파일들이 위치하는 영역

- Staging Area : Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

- Repository : **버전(commit)** 이력과 파일들이 영구적으로 저장되는 영역
  
  모든 **버전(commit)** 과 변경 이력이 기록됨
  
  ###### commit : 변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다하여 'snapshot' 이라고도 함

###### Git의 동작(명령어)

- git init : 로컬 저장소 설정(초기화) -> git의 버전 관리를 시작할 디렉토리에서 진행
  
  ###### git init 주의사항
  
  - git 로컬 저장소 내에 또 다른 git 로컬 저장소를 만들지 말 것
  
  - 즉, 이미 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력X
  
  - git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git 저장소가 안쪽의 git 저장소의 변경사항을 추적할 수 없기 때문

- git add : 변경사항이 있는 파일을 staging area에 추가

- git commit : staging area에 있는 파일들을 저장소에 기록 -> 해당 시점의 버전을 생성하고 변경 이력을 남기는 것

- git status : 현재 로컬 저장소의 파일 상태 보기

- git log : comit history 보기

- git log --oneline : commit 목록 한 줄로 보기

- git config --global -l : git global 설정 정보 보기
  
  ![이미지](https://postfiles.pstatic.net/MjAyMzA3MTNfMjE4/MDAxNjg5MjM0ODc0NjUw.oSjAyJs_VASHkDREXzQniuUS-yR_llCj-b4SeDWzZu4g.XD3TAbdcpKwRTOkZ5PMpkFovMhvn_tCU81q_5cJP0mAg.PNG.bestar96/image.png?type=w773)
  
  ---
  
  ---
  
  ---
