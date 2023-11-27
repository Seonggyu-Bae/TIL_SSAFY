from sys import stdin

input = stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve(i, j, dir):
    global ans
    if cleaning[i][j] == 0:
        ans += 1
        cleaning[i][j] = 1

    flag = False
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0 and cleaning[ni][nj] == 0:
            flag = True
            break

    if flag:
        if dir == 0:
            if 0 <= j - 1 and room[i][j - 1] == 0 and cleaning[i][j - 1] == 0:
                solve(i, j - 1, 3)
            else:
                solve(i,j,3)

        elif dir == 1:
            if 0 <= i - 1 and room[i - 1][j] == 0 and cleaning[i - 1][j] == 0:
                solve(i - 1, j, 0)
            else:
                solve(i,j,0)

        elif dir == 2:
            if j + 1 < M and room[i][j + 1] == 0 and cleaning[i][j + 1] == 0:
                solve(i, j + 1, 1)
            else:
                solve(i,j,1)

        else:
            if i + 1 < N and room[i + 1][j] == 0 and cleaning[i + 1][j] == 0:
                solve(i + 1, j, 2)
            else:
                solve(i,j,2)

    else:
        if dir == 0:
            if i + 1 < N and not room[i + 1][j]:
                solve(i + 1, j, 0)
            else:
                return
        elif dir == 1:
            if 0 <= j - 1 and not room[i][j - 1]:
                solve(i, j - 1, 1)
            else:
                return
        elif dir == 2:
            if 0 <= i - 1 and not room[i - 1][j]:
                solve(i - 1, j, 2)
            else:
                return
        else:
            if j + 1 < M and not room[i][j + 1]:
                solve(i, j + 1, 3)
            else:
                return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cleaning = [[0] * M for _ in range(N)]
ans = 0

solve(r, c, d)
print(ans)
