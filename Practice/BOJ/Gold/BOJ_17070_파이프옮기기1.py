from sys import stdin


def solve(i, j, sta):
    global ans

    if i == N - 1 and j == N - 1:
        ans += 1
        return

    # 가로
    if sta == 0:
        if j + 1 < N and homeinfo[i][j + 1] == 0:
            solve(i, j + 1, 0)
        if i + 1 < N and j + 1 < N and homeinfo[i][j + 1] == 0 and homeinfo[i + 1][j] == 0 and homeinfo[i + 1][
            j + 1] == 0:
            solve(i + 1, j + 1, 1)

    # 대각
    elif sta == 1:
        if j + 1 < N and homeinfo[i][j + 1] == 0:
            solve(i, j + 1, 0)
        if i + 1 < N and homeinfo[i + 1][j] == 0:
            solve(i + 1, j, -1)
        if i + 1 < N and j + 1 < N and homeinfo[i][j + 1] == 0 and homeinfo[i + 1][j] == 0 and homeinfo[i + 1][
            j + 1] == 0:
            solve(i + 1, j + 1, 1)
    # 세로
    else:
        if i + 1 < N and homeinfo[i + 1][j] == 0:
            solve(i + 1, j, -1)

        if i + 1 < N and j + 1 < N and homeinfo[i][j + 1] == 0 and homeinfo[i + 1][j] == 0 and homeinfo[i + 1][
            j + 1] == 0:
            solve(i + 1, j + 1, 1)


N = int(stdin.readline().rstrip())

homeinfo = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
status = 0
ans = 0

solve(0, 1, 0)

print(ans)
