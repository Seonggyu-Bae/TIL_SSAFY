T = int(input())
for tc in range(1,T+1):
    N = int(input())

    bus_stop = [0] * 5001

    for _ in range(N):
        Ai, Bi = map(int, input().split())
        for i in range(Ai,Bi+1):
            bus_stop[i] +=1

    print(f'#{tc}', end=' ')
    P = int(input())
    for _ in range(P):
        C = int(input())
        print(bus_stop[C],end=' ')

    print()