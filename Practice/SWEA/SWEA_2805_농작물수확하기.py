T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    N_half = N//2
    my_farm = [list(map(int, input())) for _ in range(N)]
    profit = 0

    for i in range(N_half + 1):
        for j in range(N_half - i, N_half + i + 1):
            profit += my_farm[i][j]

    temp = 0
    for i in range(N-1, N_half, -1):
        temp += 1
        for j in range(N_half-temp+1, N_half + temp):
            profit += my_farm[i][j]

    print(f'#{tc} {profit}')
