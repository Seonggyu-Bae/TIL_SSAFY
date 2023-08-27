T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [0]

    for _ in range(N):
        x, y, way, k = map(int, input().split())
