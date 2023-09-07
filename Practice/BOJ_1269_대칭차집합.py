A,B = map(int, input().split())

a = set(map(int,input().split()))
b = set(map(int,input().split()))

temp = a & b
print(A+B - 2*len(temp))