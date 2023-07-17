T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    A = list
    for i in range(N):
        A[i] = (map(int, input().split()))

    print(f'#{test_case}')

    for i in range(N):
        for j in range(N-1,-1):
            print(f'{A[j][i]}',end="")
        print(' ',end="")
        for k in range(N-1,-1):
            print(f'{A[N-i-1][j]}',end="")  
        print(' ',end="")
        for l in range(N):
            print(f'{A[l][N-i-1]}',end="")
        print('')