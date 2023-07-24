# main.py

def find_min_max(my_list):
    #리스트 정렬
    new_list = sorted(my_list)
    #처음과 마지막 값을 튜플로 선언
    min_max = (new_list[0],new_list[len(new_list)-1])
    #반환
    return min_max

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)
