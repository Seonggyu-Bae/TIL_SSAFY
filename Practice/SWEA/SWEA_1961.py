#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # 2차원 배열 입력
    A = [list(map(int,input().split())) for _ in range(N)]

   
    print(f'#{test_case}')
    
    for i in range(N):

        # 각 회전(90, 180, 270도)의 1행 출력
        for j in range(N-1,-1,-1):
            print(f'{A[j][i]}',end="")

        print(' ',end="")

        # 각 회전의 2행 출력
        for k in range(N-1,-1,-1):
            print(f'{A[N-i-1][k]}',end="")  

        print(' ',end="")

        # 각 회전의 3행 출력
        for l in range(N):
            print(f'{A[l][N-i-1]}',end="")

        print('')