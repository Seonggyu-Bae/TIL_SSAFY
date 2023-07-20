import ws_4_3

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

censored_user_list = []
u_list = {}
def create_user(user_list):
    for i in range(len(user_list)):
        u_list.update({ 'na' : user_list[i]['name'] , 'comp': user_list[i]['company']})
        if censorship(u_list) == True:
            censored_user_list.append({u_list['na'],u_list['comp']})

    return dict(censored_user_list)     



def censorship(info):
    if info['comp'] in black_list:
        print(f"{info['comp']} 소속의 {info['na']} 은/는 등록할 수 없습니다. ")
        return False
    else:
        print('이상 없습니다.')
        return True

  
print(create_user(ws_4_3.dummy_data))