import sys

N, M, q = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
query = [list(map(int, sys.stdin.readline().split())) for _ in range(q)]
for i in range(q):
    if query[i][0] == 0:
        matrix[query[i][1]][query[i][2]] = query[i][3]
    else:
        matrix[query[i][1]], matrix[query[i][2]] = matrix[query[i][2]], matrix[query[i][1]]

for i in range(N):
    print(*matrix[i])