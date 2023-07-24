# 메서드란? 
# 클래스 안에 선언된 함수를 뜻한다.
# 클래스는 객체를 생성하기 위해서 작성함
# 메서드를 사용하는 방법 : 객체.메서드이름()

print('hello'.capitalize())
'hello'

#문자열 '54321' 로 만들어 출력
lst = [5, 4, 3, 2, 1]

#result = '.join(lst) -> 오류 각 요소가 문자열이 아님

map(str,lst) # lst의 각 요소를 문자열로 만듬

result = ''.join(map(str,lst))

print(result)
