# 혈액형 인원수 세기
# {'A' : 3, 'B' : 3, 'o' : 3, 'AB' : 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

#[]
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    #기존에 이미 키가 존재한다면
    if blood_type in new_dict:
        #기존 키의 값을 1 증가
        new_dict[blood_type] += 1
    #키가 존재하지 않는다면(처음설정되는키)
    else:
        new_dict[blood_type] = 1    

print(new_dict)

#.get() 활용
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    new_dict[blood_type] = new_dict.get(blood_type,0) + 1    

print(new_dict)


#.setdefault()
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    new_dict.setdefault(blood_type,0)
    new_dict[blood_type] += 1

print(new_dict)
