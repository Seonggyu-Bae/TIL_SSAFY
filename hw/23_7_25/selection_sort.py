"""
selection sort 예시



"""

def sort_tuple(my_tuple):
    lst = list(my_tuple)
    
    # i 번째 자리에 숫자 찾아 넣기
    # 제일 작은 숫자를 찾기 위해서 가장 작은 수의 위치를 저장하는 변수
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min_idx]:
                min_idx = j
        # 제일 작은 인덱스를 찾았음
        # i 번째 자리에 들어갈 요소를 찾았으니 i번째 자리와 min_idx자리를 교환
        lst[i] , lst[min_idx] = lst[min_idx], lst[i]  
        #파이썬은 이렇게 동시에 변경이 가능함
        #C에서는 temp만들어서 했었음
        
    return tuple(lst)



result = sort_tuple((5, 2, 8, 1, 3))
print(result)
