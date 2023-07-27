class UserInfo:

    def __init__(self):
        self.user_data = {'name': '\n', 'age' : '\n'}
    
    def get_user_info(self):
        try:
            user_name = input('이름을 입력하세요: ')
            self.user_data['name'] = user_name
            user_age = int(input('나이를 입력하세요: '))
            self.user_data['age'] = user_age
            print(self.user_data['name'],self.user_data['age'])
        except ValueError: # 나이가 문자로 입력되었을 경우
            print('나이는 숫자로 입력해야 합니다.')

    def display_user_info(self):
        if self.user_data['age'] == '\n':
            pass
        elif self.user_data['name'] == '\n' or self.user_data['age'] == '\n':
            print('사용자 정보가 입력되지 않았습니다.')
        else:
            print(f'사용자 정보 : \n이름 : {self.user_data.pop("name")}\n나이 : {self.user_data.pop("age")}')

user = UserInfo()
user.get_user_info()
user.display_user_info()

