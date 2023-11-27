for tc in range(1, 11):
    t_l = int(input())
    ans = 0
    table = [list(map(int, input().split())) for _ in range(t_l)]

    # 1: N극
    # 2: S극

    for i in range(t_l):
        for j in range(t_l):
            if table[i][j] == 1:    # 한가지 극을 선택함
                temp = i+1
                while temp < t_l:           # 범위 안벗어나게 아래로 탐색
                    if table[temp][j] == 2: # 밑에 성질다른 자성체가있으면 있으면 교착상태임
                        ans += 1
                        break
                    elif table[temp][j] == 1:   # 근데 같은게 먼저 나오면 걔부터 탐색하면되니까 끝내줌
                        break
                    else:                       # 둘다아니면(0) 아래로 계속 탐색
                        temp += 1

    print(f'#{tc} {ans}')
