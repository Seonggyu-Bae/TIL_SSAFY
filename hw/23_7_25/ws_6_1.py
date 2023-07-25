#주어진 셋에서 두 개의 셋을 합친 결과를 반환하는 union_sets 함수를 작성하시오.
#두 개의 셋을 인자로 받아 합집합을 반환해야 한다.

def union_sets(*my_sets):
    u_sets = set()

    for my_set in my_sets:
       u_sets = u_sets.union(my_set)

    return u_sets

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
