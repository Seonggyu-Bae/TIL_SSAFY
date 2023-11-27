T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card_name = input().split()

    print(f'#{tc}', end=' ')

    if N % 2 == 0:
        for i in range(N//2):
            print(card_name[i], end=' ')
            print(card_name[N//2 + i], end=' ')
    else:
        for i in range(N//2+1):
            print(card_name[i], end=' ')
            if N//2 + i+1 < N:
                print(card_name[N//2 + i+1], end=' ')

    print()
