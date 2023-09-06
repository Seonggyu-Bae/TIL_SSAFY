import sys

N, M = map(int, sys.stdin.readline().split())

nohear = [None]*N
nohearsee = []
count = 0
for i in range(N):
    nohear[i] = sys.stdin.readline()
for i in range(M):
    nosee = sys.stdin.readline()
    if nosee in nohear:
        count += 1
        nohearsee.append(nosee)


print(count)
for x in nohearsee:
    print(x)