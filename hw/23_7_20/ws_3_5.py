# 실습 번호.py
import book

number_of_people = 0


def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    print(f'{name}님 환영합니다 !')
    temp = {}
    temp['name'] = name
    temp['age'] = age
    temp['address'] = address

    return temp

many_user = list(map(create_user, name, age, address))

info = {}
info = map(lambda x: x['name'],many_user)
info = map(lambda y: +y['age'],many_user)
print(list(info))

'''
def rental_book(info):
    info('age') % 10 = rental_book

    book.decrease_book(info.age%10)
    print(f'{info.name}님이 {info.age%10}권의 책을 대여하였습니다')
'''