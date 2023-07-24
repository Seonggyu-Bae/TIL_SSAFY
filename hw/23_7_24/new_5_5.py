# ws_5_5.py

# 리스트에서 홀수를 모두 제거하고 짝수만 남긴 리스트를 반환하는 함수
# extend와 pop을 활용하여 구현해야함
def even_elements(my_list):
    new_list = []
    new_list.extend(my_list)
    i = 0
    temp = 0
#for로 돌리면 idx 에러 발생해서 while로 구현함
    while i==0:
        #반복할때마다 list의 길이를 구하고
        my_len = len(new_list)
        
        for idx in range(temp,my_len):# 검사를 효율적으로 하기위해 인덱스 설정
            #홀수면 pop하고 break한다(안하면 idx에러남)
            if new_list[idx] % 2 == 1:
                new_list.pop(idx)
                break
            #모든 항목을 다 검사했으면 종료해야하니까 i를 바꿔서 종료
            if idx == my_len-1:
                i = 1

            temp += 1 # 검사를 효율적으로 하기위해 인덱스
           
    return new_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
