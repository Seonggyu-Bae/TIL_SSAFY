number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(user_name, user_age, user_add):
    for i in range(len(user_name)):
        print(f'{user_name[i]}님 환영합니다!')
        increase_user()
        user_info = {'name' : user_name[i], 'age' : user_age[i], 'address' : user_add[i]}
    return (user_info)

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

print(create_user(name,age,address))
print(number_of_people)