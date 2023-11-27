from collections import deque
from sys import stdin

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve(info):
    Q = info

    while Q:
        sx, sy = Q.popleft()
        visited[sy][sx] = 1
        for d in range(4):
            nx, ny = sx + di[d], sy + dj[d]
            if 0 <= nx < M and 0 <= ny < N and ground[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = visited[sy][sx] + 1
                Q.append((nx, ny))


T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, stdin.readline().split())
    location = deque(list(map(int, (stdin.readline().split()))) for _ in range(K))
    ground = [[0] * M for _ in range(N)]

    for i in range(K):

        ground[location[i][1]][location[i][0]] = 1

    visited = [[0] * M for _ in range(N)]

    solve(location)

    print(visited)
