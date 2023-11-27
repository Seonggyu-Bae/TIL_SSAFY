import math
N = int(input())

factorial_N = math.factorial(N)
temp = list(str(factorial_N))
count = 0
for idx in reversed(temp):
    if idx == '0':
        count += 1
    else:
        break

print(count)


