N = int(input())

count = 0

for num in range(1,N+1):
    s = str(num)
    temp = s.count("3") + s.count("6") + s.count("9")
    count += temp
    
print(count)            