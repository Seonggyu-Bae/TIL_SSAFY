print('hello', end = ' ')
print('world')

numbers = [1, 2, 3]
result = map(str, numbers)

print(result) #<map object at 0xfaffgfaga34>
print(list(result)) #['1', '2', '3']



result = []
for number in numbers:
    result.append(str(number))

print(result)


#map + lambda

numbers = [1,2,3,4,5]
result = list(map(lambda x: x * 2, numbers))

print(result)