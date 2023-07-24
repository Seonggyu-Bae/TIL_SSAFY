N,M = map(int, input().split())

S = set()
check_str = ''
count = 0

for i in range(N):
    S.add(input())


for i in range(M):
    check_str = input()
    if check_str in S:
        count += 1

print(count)