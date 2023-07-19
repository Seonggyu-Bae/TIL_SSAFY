is_done = True

lst1 =[1,2,3]

if not is_done:
    print(lst1)

#list가 비어있지 않으면 실행


# 리스트는 비어있지 않으면 True임
if lst1:
    print('리스트에 뭔가 저장되어있습니다')
    print(lst1)



lst2 = []

#list가 비어있으면 실행
if not lst2:
    print('리스트가 비어있습니다')


'''
Packing : 여러 개의 값을 하나의 변수에 묶어서 담는 것
        -변수에 담긴 값들은 튜플 형태로 묶임

Unpacking : 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것

'''
print('packing example')
packed_values = 1, 2, 3, 4, 5
print(packed_values) #(1, 2, 3, 4, 5) 튜플 형태로 묶임
a,b = 1,2
#a,b = 1, 2, 3, 4, 5
print(a)
print(b)




# a,b = 1,2,3 unpack 하려면 2개만 있어야함 
a,*b = 1, 2, 3, 4, 5 #1만 a에 나머지는 b에

print(a)
print(b)

*a,b = 1, 2, 3, 4, 5 #5만 b에 나머지는 a에
print(a)
print(b)

a, *b, c = 1,2,3,4,5
print(a)
print(b)
print(c)


## unpacking
lst = [1, 2, 3, 4, 5, 6]

print(*lst)


#임의의 인자 목록

#인자로 받은 모든 수의 합을 출력하는 함수
def my_sum(*args):
    print(sum(args))


my_sum(1,2,3,4,5,6,124531,53163156)

# my_sum(lst) -> 타입에러
my_sum(*lst) #언패킹해서 넣으면 가능