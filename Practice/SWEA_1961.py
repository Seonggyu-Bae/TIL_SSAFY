T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]

    print(f'#{test_case}')
    
## 아래 구현도 점검필요
    for i in range(N):
        for j in range(N-1,-1,-1):
            print(f'{A[j][i]}',end="")

        print(' ',end="")

        for k in range(N-1,-1,-1):
            print(f'{A[N-i-1][k]}',end="")  

        print(' ',end="")

        for l in range(N):
            print(f'{A[l][N-i-1]}',end="")

        print('')