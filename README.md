# 23/07/27



##### 상속 (Inheritance)

- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것



##### 상속이 필요한 이유

1. **코드 재사용**
   
   1. 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
   
   2. 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음

2. **계층 구조**
   
   1. 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
   
   2. 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음

3. **유지보수의 용이성**
   
   1. 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
   
   2. 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음





```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        #super()  : 부모 클래스의 메서드를 호출하기 위해 사용되는 내장함수
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

#부모 Person 클래스의 talk 메서드를 활용
p1.talk()
s1.talk()
```









##### 다중상속

- 두 개 이상의 클래스를 상속 받는 경우

- 상속받은 모든 클래스의 요소를 활용 가능함

- 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정**됨



```python
class Person:
    gene  = 'XYZ'

    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        return f'반갑습니다, {self.name}'


class Mom(Person):
    gene = 'XX'
    
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    mom_gene = Mom.gene

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
    
baby1 = FirstChild('아가')

print(baby1.cry())
print(baby1.swim())
print(baby1.walk())
print(baby1.gene) #Dad가 상속 순서가 앞이기 때문에 XY를 받음
print(baby1.mom_gene)


print(FirstChild.mro()) 
```



##### 상속 관련 함수와 메서드

- mro()
  
  - Method Resolution Order
  
  - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하느 메서드
  
  - 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속관계에 있으면 인스턴스 -> 자식클래스 -> 부모클래스로 확장



#### 에러와 예외



##### 디버깅



###### 버그(bug) : 소프트웨어에서 발생하는 오류 또는 결함 프로그램의 예상된 동작과 실제 동작 사이의 불일치



##### Debugging : 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정, 프로그램의 오작동 원인을 식별하여 수정하는 작업



##### 디버깅 방법

1.  print 함수 활용
   
   1. 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각

2.  개발환경에서 제공하는 기능 활용
   
   1. breakpoint, 변수 조회 등

3.  Python tutor 활용(단순 파이썬 코드인 경우) 

4.  뇌 컴파일, 눈 디버깅 등



##### 에러(Error) 프로그램 실행 중에 발생하는 예외 상황

###### 파이썬의 에러 유형

1. 문법 에러(Syntax Error)
   
   - 프로그램의 구문이 올바르지 않은 경우(오타, 괄호 및 콜론 누락 등 문법적오류)
   
   - 
     

2. 예외(Exception)
   
   - 프로그램 실행 중에 감지되는 에러
   
   

##### 

##### 내장 예외 (Bulit-in Exceptions)

- 예외 상황을 나타내는 예외 클래스들
  
  - 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용





##### 예외 처리

###### try와 except : 파이썬에서는 <u>try</u> 문과 <u>except</u> 절을 사용하여 예외 처리



##### try-except 구조

- try 블록 안에는 예외가 발생할 수 있는 코드를 작성

- except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성

- 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

- ```python
  try:
      #예외 발생 가능한 코드
  
  except 예외:            
      #예외 처리 코드
  ```

- ```python
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print('0으로 나눌 수 없습니다.')    
  
  try:
      num = int(input('숫자입력 : '))
  except ValueError:
      print('숫자가 아닙니다.')
  ```

###### 복수 예외 처리연습

- ```python
  try:
      num = int(input('100으로 나눌 값을 입력하시오 : '))
      print(100 / num)
  except ValueError:
      print('숫자를 넣어주세요.')    
  except ZeroDivisionError:
      print('0으로 나눌 수 없습니다.')    
  except:
      print('에러가 발생하였습니다.')
  ```



##### 내장 예외의 상속 계층구조 주의

- 내장 예외 클래스는  상속 계층구조를 가지기 때문에 except절로 분기시 **반드시 하위 클래스를 먼저 확인 할 수있도록 작성**해야함



### 예외처리와 값 검사에 대한 2가지 접근 방식

#### EAFP & LBYL

##### EAFP (Easier to Ask for Forgiveness than Permission)

- 예외처리를 중심으로 코드를 작성하는 접근 방식 (try - except)



###### LBYL (Look Before You Leap)

- 값 검사를 중심으로 코드를 작성하는 접근 방식 (if - else)
  
  

| EAFP                                                         | LBYL                                             |
|:------------------------------------------------------------:|:------------------------------------------------:|
| 일단 실행하고 예외를 처리                                               | 실행하기 전에 조건을 검사                                   |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행                                   | 코드 실행전에 조건문 등을 사용하여 예외 상황을 미리 검사하고 예외 상황을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라, 예외가 발생한 후에 예외를 처리 | 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수있음        |
| 예외 상황을 예측하기 어려운 경우에 유용                                       | 예외 상황을 미리 방지하고 싶을 때 유용                           |







---





# 23/07/26

#### 절차 지향 프로그래밍

- 프로그램을 '데이터'와 '절차'로 구성하는 방식의 프로그래밍 패러다임

- "데이터"와 해당 데이터를 처리하는 **"함수(절차)"가 분리**되어 있으며, 함수 호출의 흐름이 중요

- **코드의 <u>순차적인 흐름</u>과 <u>함수 호출</u>에 의해 프로그램이 진행**

- 실제로 실행되는 내용이 무엇이 무엇인가가 중요

- 데이터를 다시 재사용하거나 하기보다는 처음부터 끝까지 실행되는 결과물이 중요

##### 소프트웨어 위기

- 하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격

- 절차 지향으로는 해결하기 힘듬

#### OOP : 객체 지향 프로그래밍

- 데이터(객체)와 해당 데이터를 조작하는 메서드(함수)를 하나의 객체로 묶어 관리하는 방식

- 객체 간  상호작용과 메시지 전달이 중요

#### 클래스(class)

- 파이썬에서 **타입을 표현하는 방법**

- 객체를 생성하기 위한 설계도(blueprint)

- 데이터와 기능을 함께 묶는 방법을 제공

#### 객체(object)

- 클래스에서 정의한 것을 토대로 메모리에 할당된 것

- '**속성**'과 '**행동**'으로 구성된 모든 것

###### 클래스와 객체

- 클래스로 만든 객체를 인스턴스라고도함

- 가수(클래스)
  
  - 아이유는 객체다(O)
  
  - 아이유는 인스턴스다(X)
  
  - 아이유는 가수의 인스턴스다(O)

- 문자열 타입(클래스)의 객체(인스턴스)
  
  - '',  'hello', '파이썬'

- 리스트 타입(클래스)의 객체(인스턴스)
  
  - [1, 2, 3], [1], [], ['hi']

- "hello".upper()
  
  - 문자열.대문자로()
  
  - 객체.행동()
  
  - **인스턴스.메서드()**

#### <u>하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.</u>

#### 객체(object)의 특징

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가

- 속성(attribute) : 어떤 상태(데이터)를 가지는가?

- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

- 객체(Object) = 속성(Attribute) + 기능(Method)

##### 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성

- 인스턴스를 만들면, 인스턴스 객체가 생성되고 **독립적인** 이름 공간 생성

- 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색

##### 독립적인 이름공간을 가지는 이점

1. 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능

2. 객체 지향 프로그래밍의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장

3. 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음

4. 따라서 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌

#### 메서드

- 메서드 종류
  
  - 인스턴스 메서드
  
  - 클래스 메서드
  
  - 정적 메서드

##### 인스턴스 메서드(instance method)

##### 클래스로 부터 생성된 각 인스턴스에서 호출할 수 있는 메서드

- 인스턴스의 상태를 조작하거나 동작을 수행

**인스턴스 메소드 구조**

- 클래스 내부에 정의되는 메서드의 기본

- 반드시 첫 번째 매개변수로 **인스턴스 자신(self)** 을 전달받음

- ```python
  class Myclass:
  
      def instance_method(self, arg1, ...):
          pass
  ```

- Self 동작 원리
  
  - upper 메서드를 사용해 문자열 대문자로 변경하기 -> 'hello'. upper()
  
  - 실제 파이썬 내부동작 - > str.upper('hello')
  
  - str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것이다.
  
  - **<mark>인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기 자신인 이유</mark>**
  
  - 'hello'.upper()은 str.upper('hello')를 객체 지향 방식의 메서드로 호출하는 표현이다. ( 단축형 호출)
  
  - 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌 **객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적 표현이다.**
    
         

##### 클래스 메서드(class method)

###### 클래스가 호출하는 메서드

- **클래스 변수를 조작하거나 클래스 레벨의 동작을 수행**

###### 클래스 메서드 구조

- @classmethod 데코레이터를 사용하여 정의

- 호출 시, 첫번째 인자로 호출하는 클래스(cls)가 전달됨

- ```python
  class Myclass:
  
      @classmethod
      def class_method(cls, arg1, ...):
          pass
  ```

###### 스태틱(정적) 메서드 (static method)

- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드

- 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용

###### 스태틱 메서드 구조

- @staticmethod 데코레이터를 사용하여 정의

- 호출 시 필수적으로 작성해야 할 매개변수가 없음

- **즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용**

- ```python
  class Myclass:
  
      @staticmethod
      def static_method(arg1, ...):
          pass
  ```

##### 메서드 정리

- 인스턴스 메서드
  
  - 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행

- 클래스 메서드
  
  - 인스턴스의 상태에 의존하지 않는 기능을 정의
  
  - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

- 스태틱 메서드
  
  - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

```python
class MyClass:

    def instance_method(self):
        return 'instance method', self


    @classmethod
    def class_method(cls):
        return 'class method', cls


    @staticmethod
    def static_method():
        return 'static method'
```

###### 클래스가 할 수 있는 것

- 클래스는 모든 메서드를 호출 할 수있음

- **<mark>하지만 클래스는 클래스 메서드와 스태틱 메서드만 사용하도록 한다</mark>**

- ```python
  instance = Myclass()
  
  print(Myclass.instance_method(instance)) # ('instance method', <__main.Myclass object at0x..fad>))
  print(Myclass.class_method()) #('class method', <class '__main__.Myclass>)
  print(Myclass.static_method()) # static method
  ```

###### 인스턴스가 할 수 있는 것

- 인스턴스는 모든 메서드를 호출 할 수 있음

- **<mark>하지만 인스턴스는 인스턴스 메서드만 사용하도록 한다</mark>**

- ```python
  instance = Myclass()
  
  print(instance .instance_method(instance)) # ('instance method', <__main__.Myclass object at0x..fad>))
  print(instance .class_method()) #('class method', <class '__main__.Myclass>)
  print(instance .static_method()) # static method
  ```

##### 참고

##### 매직 메서드

- 특별한 인스턴스 메서드

- 특정 상황에 자동으로 호출되는 메서드

- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
  
  - 스페셜 메서드 혹은 매직 메서드라고 불림

- 예시
  
  - @

#### 절차 지향과 객체 지향은 대조되는 개념이 아니다.

###### 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임

----

# 23/07/25

```python
a = [
    { 
        'name': 'pasta',
        'price': 10000
    },
    {
        'name': 'hamburger',
        'price': 10000
    }
]


b = {
    'pasta' : 10000,
    'hamburger': 10000
}
```

#### a는 선형탐색

#### b는 키로 찾음 해시함수, 해시테이블 , 세트요소 & 딕셔너리 키

그래서 list랑 set랑 같은 원소를 가지고있어도  set가 빠른듯?

# 

----

# 23/07/20

### 제어문(Control Statement)

- 코드의 실행 흐름을 제어하는데 사용되는 구문

- **조건**에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행

### 조건문(Conditional Statement)

- 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

- 'if ' statement
  
  ```python
  dust = 35
  
  if dust > 150:
      print("So Bad")
      if dust > 300:
          print("Fucking Bad Don't Go Outside")
  elif dust > 80:
      print("Bad")
  elif dust > 30:
      print("SoSo")
  else:
      print("Good")
  ```

### 반복문(Loop Statament)

- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
  
  - 특정 작업을 반복적으로 수행
  
  - 주어진 조건이 참인 동안 반복해서 실행

### For

- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

```python
for variable in iterable:
    code block

#example

items = ['apple', 'banana', 'coconut']


for item in items:
    print(item)

"""
apple
banana
coconut
"""
```

- 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행

- 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행

- 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행

**반복 가능한 객체(iterable) :  반복문에서 순회할 수있는 객체**

- 시퀀스 객체 뿐만 아니라 dict, set 등도 포함

```python
country = 'Korea'

for char in country:
    print(char)

"""
K
o
r
e
a
"""

#------------------------------------------------------

for i in range(5):
    print(i)

"""
0
1
2
3
4
"""

#-----------------------------------------------------

numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

# [8, 12, 20, -16, 10]

#---------------------------------------------------

outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)

"""
Ac
Ad
Bc
Bd
"""

#-----------------------------------------------------

elements = [['A','B'],['c','d']]

for elem in elements:
    print(elem)

"""
['A','B']
['c','d']
"""


for elem in elements:
    for item in elem:
        print(item)

"""
A
B
c
d
"""
```

### while

- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행

- 조건식이 거짓(False)가 될 때 까지 반복

```python
while conditional_expression:
    code block

#example

a=0

while a < 3:
    print(a)
    a+=1

print('끝')

"""
0
1
2
끝
"""

#----------------------------------------------

number = int(input('type posivie int: '))

while number <= 0:
    if number < 0:
        print("음수를 입력했습니다.")
    else:
        print("0은 양의 정수가 아닙니다.")
    number = int(input(''type posivie int: '))

print('Good Job!')
```

### while 문은 반드시 **<u>종료 조건</u>**이 필요

### 적절한 반복문 활용하기

- for
  
  - 반복 횟수가 명확하게 정해져 있는 경우에 유용
  
  - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

- while
  
  - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
  
  - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

### 반복 제어

##### for 문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만,

##### 때때로 일부만 실행하느 것이 필요할 때가 있음

- break : 반복을 즉시 중지

- continue : 다음 반복으로 건너뜀

##### break 예시

```python
number = int(input('insert positive integer: ')


while number <=0:
    if number == -9999:
        print('program will shut down.')
        break

    if number < 0:
        print('you insert negative integer')
    else:
        print('0 is not positive integer')

    number = int(input('insert posivie integer plz..: ')

print(f'your input_number is {number}')

#----------------------------------------------------------------

numbers = [1,3,5,6,7,9,10,11]
found_even = False

for num in numbers:
    if num % 2 == 0:
    print('find first even number:',num)
    found_even = True
    break

if not found_even:
    print('Can't find even number')
```

##### continue 예시

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 ==0:
        continue
    print(num)

"""
1
3
5
7
9
"""
```

#### break 와 continue 주의사항

- break와 continue를 남용하는 것은 코드의 가독성을 저하시킬 수 있음

- **특정한 종료 조건**을 만들어 break를 대신하거나, **if 문을 사용**해 continue 처럼 코드를 건너 뛸 수도 있음

- 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고 코드의 의도를 명확하게 작성하도록 노력하는 것이 중요

### List Comprehension : 간결하고 효율적인 리스트 생성 방법

```python
# List Comprehension 구조
# [expression for variable in iterable]
# list(expression for variable in iterable)


# 사용전 
numbers = [1,2,3,4,5]
squared_num = []


for num in numbers:
    squaraed_num.append(num**2)


#사용후 

numbers_1 = [1,2,3,4,5]
squared_num_1 = [num**2 for num in numbers_1]
```

###### 참고 List Comprehension과 if 조건문

[expression for 변수 in iterable if 조건식]

list(expression for 변수 in iterable if 조건식)

###### 참고

- pass : 아무런 동작도 수행하지 않고 넘어가는 역할
  
  - 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지않아야 할 때 사용

- pass 예시
  
  - 코드 작성 중 미완성 부분
    
    - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일 하는 동안 오류가 발생 하지 않음
  
  ```python
  def my_function():
      pass
  ```

- 조건문에서 아무런 동작을 수행하지 않아야 할 때
  
  ```python
  if condition:
    pass # nothing to do
  else:
    #some code here
  ```

- 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법

```python
while True:
    if condition:
        break
    elif condition:
        pass
    else:
        print('..')
```

## enumerate

##### enumerate(iterable, start=0)

##### iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

```python
fruits = ['apple', 'banana', 'cherry']


for index, fruit in enumerate(fruits):
    print(f'index {index}: {fruits}')


"""
index 0: apple
index 1: banana
index 2: cherry
"""
```

---

# 23/07/19

#### 함수(Functions) : 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

- 왜 함수를 사용하는가?
  
  - 재사용성이 높아지고, 코드의 가독성과 유지보수성 향상

```python
def get_sum(num1, num2): # num1, num2: parameter (input)

    """이것은 두 수를 받아
        두 수의 합을 반환하는 함수 입니다.
        get_sum(1,2)
        3
    """

    return num1 + num2 #return value (output)
```

- 함수 정의
  
  - 함수 정의는 def 키워드로 시작
  
  - def 키워드 이후 함수 이르 작성
  
  - 괄호안에 매개변수를 정의할 수 있음
  
  - 매개변수는 함수에 전달되는 값을 나타냄

- 함수 body
  
  - 콜론(:) 다음에 들여쓰기 된 코드 블록
  
  - 함수가 실행 될 때 수행되는 코드를 정의
  
  - Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명서

- 함수 반환 값
  
  - 함수는 필요한 경우 결과를 반환할 수 있음
  
  - return 키워드 이후에 반환할 값을 명시
  
  - return문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
  
  - 반환 값이 없는 함수는 None이 return됨

### 매개변수와 인자

- **매개변수(parameter) : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수**

- **인자(argument) : 함수를 호출할 때, 실제로 전달되는 값**

##### 인자의 종류

```python
def greet(name, age=30):
    print(f,'안녕하세요, {name}님! {age}살이시군요.')



greet(name='Dave', age=35)    #안녕하세요, Dave님! 35살이시군요.
greet(24, 40)                 #안녕하세요, 24님! 40살이시군요.
greet(24,)                    #안녕하세요, 24님! 30살이시군요.
greet(age = 20, name='Dave')  #안녕하세요, Dave님! 20살이시군요.
greet(age = 20,'Dave')        #Position 오류
```

1. **위치인자 : 함수 호출 시 인자의 위치에 따라 전달되는 인자**
   
   1. 위치인자는 함수 호출 시 반드시 값을 전달해야함

2. **기본인자 :  함수 정의에서 매개변수에 기본 값을 할당하는 것**
   
   1. 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

3. **키워드 인자 : 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자**
   
   1. 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수있음
   
   2. 인자의 순서는 중요하지않고, 인자의 이름을 명시하여 전달
   
   3. **<u>단 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함</u>**

4. **임의의 인자 목록 : 정해지지 않은 개수의 인자를 처리하는 인자**
   
   1. 함수 정의 시 매개변수 앞에 **'*'** 를 붙여 사용, 여러 개의 인자를 tuple로처리

```python
def caculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')


caculate_sum(1,2,3) #합계: 6
```

5. **임의의 키워드 인자 목록 : 정해지지 않는 개수의 키워드 인자를 처리하는 인자**
   
   1. 함수 정의 시 매개변수 앞에 ****** 를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리    

```python
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30) # {'name : 'Eve', 'age' : 30}
```

#### 함수와 Scope

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

- scope
  
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  
  - local scople : 함수가 만든 scople (함수 내부에서만 참조 가능)

- variable
  
  - global variable : global scope에 정의된 변수
  
  - local variable : local scope에 정의된 변수

```python
def func():
    num = 20
    print('local',  num) #local 20

func()

print('global', num) #NameError : name 'num' is not defined
```

- num은 local scope에 존재하기 때문에 global에서 사용할 수 없음

- 이는 변수의 **수명주기**와 연관있음

##### 변수 수명주기 : 변수가 선언되는 위치와 스코프에 따라 결정됨

1. **built-in scope : 파이썬이 실행돤 이후부터 영원히 유지**

2. **global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지**

3. **local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지**

**local scope < enclosed scope < global scope < built-in scope**

- **함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수없음**

- 그래도 안쓰는게 좋음

###### global 키워드

- 변수의 스코프를 전역 범위로 지정하기 위해 사용

- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

- global 키워드 선언 전에 접근하면 오류

- 매개변수에 global 사용 불가

#### 재귀 함수 : 함수 내부에서 자기 자신을 호출하는 함수

- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐

- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

- **종료 조건을 명확히**

- **반복되는 호출이 종료 조건을 향하도록 작성**

```python
def factorial(n):
    if n == 0: #종료 조건 : n이 0이면 1을 반환
        return 1
    return n * factorial(n-1) # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과반환


result = factorial(5)
print(result) #150
```

###### 유용한 내장 함수

1. **map(function, iterable)**
   
   1. 순회 가능한 데이터구조(iterable)의 모든 요소에 **함수를 적용**하고, 그 결과를 map object로 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result) #<map object at 0xfaffgfaga34>
print(list(result)) #['1', '2', '3']
```

2. **zip(*iterables)**
   
   1. 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)


print(pair) #<zip object at 0xfaffgfaga34>
print(list(pair)) #[('jane', 'peter'), ('ashley', 'jay')]
```

##### lambda 함수 : 이름 없이 정의되고 사용되는 익명 함수

- 함수 구조 : lambda 매개변수 : 표현식

- lambda 키워드
  
  - 람다 함수를 선언하기 위해 사용되는 키워드

- 매개변수
  
  - 함수에 전달되는 매개변수들
  
  - 여러 개의 매개변수가 있을 경우 쉼표로 구분

- 표현식
  
  - 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성

```python
#map + lambda

numbers = [1,2,3,4,5]
result = list(map(lambda x: x * 2, numbers))

print(result)
```

#### 모듈(Module)

한 파일로 묶인 변수와 함수의 모음, 특정한 기능을 하는 코드가 작성된 파이선 파일(.py)

- 모듈 내 변수와 함수에 접근하려면 import문이 필요

- ex) import math

- 내장 함수 help를 사용해 모듈에 무엇이 들어있는지 확인 가능 ex) help(math)

- '.' 은 "점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라" 라는 의미의 연산자 ex) math.pi

##### 파이썬 표준 라이브러리

- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

##### 패키지

- 관련된 모듈들을 하나의 디렉토리에 모아 놓은 것

- Ex)

- my_pakage
  
  - math
    
    - my_math.py
  
  - statistics
    
    - tools.py

- 사용법

```python
from my_package.math import my_math

from my_package.statistics import tools

print(my_math.add(1,2))
print(tools.mod(1,2))
```

----

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
