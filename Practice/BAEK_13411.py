import math
N = int(input())
time = []
for _ in range(N):
    X,Y,V = map(int,(input().split()))
    distance = math.sqrt((X)**2 + (Y)**2)
    time.append(distance/V)

for _ in range(N):
    print(time.index(min[time])+1)
    
