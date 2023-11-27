import sys

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(M):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    print(sum(board[x1:x2][y1:y2]))