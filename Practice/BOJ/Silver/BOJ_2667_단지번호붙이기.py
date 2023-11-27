from collections import deque
from sys import stdin
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve(x, y):
    Q = deque()
    Q.append((x, y))
    visitied[x][y] = 1
    house = 1
    while Q:
        si, sj = Q.popleft()

        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and info[ni][nj] == 1 and not visitied[ni][nj]:
                visitied[ni][nj] = 1
                Q.append((ni, nj))
                house += 1
    return house


N = int(stdin.readline().rstrip())

info = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]

cnt = 0
total = []
visitied = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if info[i][j] == 1 and visitied[i][j] == 0:
            cnt += 1
            total.append(solve(i, j))

total.sort()

print(cnt)
for num in total:
    print(num)