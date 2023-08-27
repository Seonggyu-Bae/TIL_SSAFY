dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def my_dfs(start, n, m):
    i, j = start
    visited = [list([0] * m) for _ in range(n)]
    visited[i][j] = 1
    Q = [start]

    while Q:
        ci, cj = Q.pop(0)
        if ci == n-1 and cj == m-1:
            return visited[ci][cj]
        for d in range(4):
            ni, nj = ci + dx[d], cj + dy[d]
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] and not visited[ni][nj]:
                Q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1


N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
print(my_dfs((0, 0), N, M))
