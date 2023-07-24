# ws_5_5.py

# 리스트에서 홀수를 모두 제거하고 짝수만 남긴 리스트를 반환하는 함수
# extend와 pop을 활용하여 구현해야함
def even_elements(my_list):
    new_list =[]
    while my_list:
            el = my_list.pop()
            if el % 2 == 0:
                new_list.extend([el])

    
    return sorted(new_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
