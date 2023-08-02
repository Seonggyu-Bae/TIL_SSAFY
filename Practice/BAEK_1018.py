N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

count = 0
w_count = 0
b_count = 0

for i in range(N-7):
    for j in range(M-7):
        for k in range(i, i+8):
            for l in range(j, j+8):
