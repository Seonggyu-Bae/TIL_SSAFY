import ws_4_3

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

censored_user_list = {}
u_list = {}

def create_user(user_list):
    for user in user_list:
        name = user['name']
        company = user['company']
        u_list = {'na' : name, 'comp': company}
        if censorship(u_list) == True:
            if company not in censored_user_list:
                censored_user_list[company] = [name] #회사명을 키로, 사용자 이름을 값으로 리스트 추가
            else:
                censored_user_list[company].append(name) #회사명이 딕셔너리에 있으면 사용자 이름을 해당 리스트에 추가
    return censored_user_list            



def censorship(info):
    if info['comp'] in black_list:
        print(f"{info['comp']} 소속의 {info['na']} 은/는 등록할 수 없습니다. ")
        return False
    else:
        print('이상 없습니다.')
        return True

  
print(create_user(ws_4_3.dummy_data))
