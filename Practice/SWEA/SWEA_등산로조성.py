di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def my_dfs(si, sj, dist, cut_max):
    global ans

    if dist > ans:
        ans = dist
    visited[si][sj] = 1

    for d in range(4):
        ni, nj = si + di[d], sj + dj[d]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if map_info[ni][nj] < map_info[si][sj]:
                my_dfs(ni, nj, dist + 1, cut_max)
            elif cut_max and cut_max > map_info[ni][nj] - map_info[si][sj]:
                temp = map_info[ni][nj]
                map_info[ni][nj] = map_info[si][sj] - 1
                my_dfs(ni, nj, dist + 1, 0)
                map_info[ni][nj] = temp

    visited[si][sj] = 0


def find_top(n):
    t = 0
    for i in range(n):
        for j in range(n):
            if map_info[i][j] > t:
                t = map_info[i][j]

    return t


def find_top_points(n, t):
    for i in range(n):
        for j in range(n):
            if map_info[i][j] == t:
                top_points.append((i, j))


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    top = find_top(N)
    top_points = []
    find_top_points(N, top)

    ans = 0
    while top_points:
        a, b = top_points.pop()
        my_dfs(a, b, 1, K)

    print(f'#{tc} {ans}')
