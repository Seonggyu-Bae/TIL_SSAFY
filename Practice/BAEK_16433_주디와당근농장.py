N, R, C = map(int, input().split())

carrot_farm = [list(['.'] * N) for _ in range(N)]
carrot_farm[R-1][C-1] = 'v'


