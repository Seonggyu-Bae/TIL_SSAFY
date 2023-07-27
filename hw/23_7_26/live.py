# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red' # 클래스변수
    #클래스 내부에 선언된 변수
    #클래스로 생성된 모든 인스턴스들이 공유하는 변수

# 메서드
# __init__ -> 생성자 메서드     
# 객체를 생성할 때 자동으로 호출되는 메서드
# 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
    def __init__(self,name): 
        self.name = name    #인스턴스변수
        #인스턴스(객체)마다 별도로 유지되는 변수
        #인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때 마다 초기화

    #인스턴스 메서드
    def singing(self):
        return f'{self.name}(이/가) 노래합니다.'
    #각각의 인스턴스에서 호출할 수있는 메서드
    #인스턴스 변수에 접근하고 수정하는 등의 작업 수행

# (Person 클래스의) 인스턴스 생성    
singer1 = Person('아이유')
singer2 = Person('나얼')
# 메서드 호출
print(singer1.singing())
print(singer2.singing())