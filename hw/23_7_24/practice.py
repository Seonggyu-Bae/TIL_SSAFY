numbers = [1,2,3]

#할당
list1 = numbers #numbers의 주소값을 보고있음

#슬라이싱
list2 = numbers[:] # 복사본을 만드는 것임 numbers의 주솟값이 아닌 list2가 보고있는 주솟값이 새로 생김

numbers[0] = 100

print(list1) # [100, 2, 3] numbers의 주소값을 보고있는 것이기에 numbers[0]을 바꾸면 그대로 따라감
print(list2) # [1, 2, 3]


#append,extend,pop
#reverse, sort


# reverse slicing example
print(numbers[-1:-3:-1])


print("dafjafkjk".capitalize())

# 매서드는 이어서 사용 가능

text = 'heLLo, woRld!'

new_text = text.swapcase().replace('l', 'z')

print(new_text)


# 리스트 더하기
lst = [1,2]
lst1 = [3,4]
lst2 = lst + lst1
print(lst2)

#
#sort와 sorted의 차이점
lst = [3,4,1,3,4,5,1,246,743]
print(lst.sort()) #정렬해줌 -> 원본을 바꿔줌
print(lst)

lst5 = [4,12531,135,462,54,43,4,252,3,541,53,43,42]
sorted(lst5) # 정렬을 한 새로운 list를 반환함 -> 원본은 그대로

print(lst5)

print(sorted(lst5))