# 진법 변경

print(bin(12))


print(2 / 3)
print(5 / 3)

#지수(제곱횟수) 표현
print(314e-2)
print(314e2)


#fstring 응용

greeting = 'hi'

print(f'{greeting:>10}')
print(f'{greeting:^10}')
print(f'{3.141592:.4f}')



#불변과 가변

my_str = 'hello'

#TypeError: 'str' object does not support item assignment
#my_str[0] ='z' 

my_list = [1,2,3]
my_list[0] = 100

print(my_list)