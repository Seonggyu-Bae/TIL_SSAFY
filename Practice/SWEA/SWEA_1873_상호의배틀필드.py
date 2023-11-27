def battlefield():
    ti, tj = tank_pos()

    for u_i in user_input:
        if u_i == 'U':
            ni = ti + -1
            if 0 <= ni < H and game_map[ni][tj] == '.' and game_map[ni][tj] != '-':
                game_map[ni][tj] = '^'
                game_map[ti][tj] = '.'
                ti = ni
            else:
                game_map[ti][tj] = '^'
        elif u_i == 'D':
            ni = ti + 1
            if 0 <= ni < H and game_map[ni][tj] == '.' and game_map[ni][tj] != '-':
                game_map[ni][tj] = 'v'
                game_map[ti][tj] = '.'
                ti = ni
            else:
                game_map[ti][tj] = 'v'
        elif u_i == 'L':
            nj = tj - 1
            if 0 <= nj < W and game_map[ti][nj] == '.' and game_map[ti][nj] != '-':
                game_map[ti][nj] = '<'
                game_map[ti][tj] = '.'
                tj = nj
            else:
                game_map[ti][tj] = '<'
        elif u_i == 'R':
            nj = tj + 1
            if 0 <= nj < W and game_map[ti][nj] == '.' and game_map[ti][nj] != '-':
                game_map[ti][nj] = '>'
                game_map[ti][tj] = '.'
                tj = nj
            else:
                game_map[ti][tj] = '>'

        else:
            t_dir = game_map[ti][tj]
            if t_dir == '^':
                temp = 0
                while True:
                    temp += 1
                    ni = ti - temp
                    if ni < 0:
                        break
                    elif game_map[ni][tj] == '*':
                        game_map[ni][tj] = '.'
                        break
                    elif game_map[ni][tj] == '#':
                        break
            elif t_dir == '>':
                temp = 0
                while True:
                    temp += 1
                    nj = tj + temp
                    if nj >= W:
                        break
                    elif game_map[ti][nj] == '*':
                        game_map[ti][nj] = '.'
                        break
                    elif game_map[ti][nj] == '#':
                        break
            elif t_dir == 'v':
                temp = 0
                while True:
                    temp += 1
                    ni = ti + temp
                    if ni >= H:
                        break
                    elif game_map[ni][tj] == '*':
                        game_map[ni][tj] = '.'
                        break
                    elif game_map[ni][tj] == '#':
                        break

            else:
                temp = 0
                while True:
                    temp += 1
                    nj = tj - temp
                    if nj < 0:
                        break
                    elif game_map[ti][nj] == '*':
                        game_map[ti][nj] = '.'
                        break
                    elif game_map[ti][nj] == '#':
                        break


def tank_pos():
    for i in range(H):
        for j in range(W):
            if game_map[i][j] == '>' or game_map[i][j] == '<' or game_map[i][j] == '^' or game_map[i][j] == 'v':
                return i, j


T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())

    game_map = [list(input()) for _ in range(H)]
    N = int(input())
    user_input = input()
    battlefield()

    print(f'#{tc}', end=' ')
    for i in range(H):
        print(*game_map[i], sep='')
