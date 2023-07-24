# ws_5_3.py

# 튜플을 인자로 받아 정렬하여 새로운 튜플로 반환하는 함수
def sort_tuple(my_tuple):
  new_tuple = tuple(sorted(my_tuple))

  return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
