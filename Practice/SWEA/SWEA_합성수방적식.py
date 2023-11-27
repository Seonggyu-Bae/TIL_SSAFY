T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 각 수에 N을 곱하면 N을 이용해서 표현 가능한 합성수
    # 두수의 차이는 N만큼 나야하기 때문에 합성수 중에 차이가 1인 것을 곱해주면됨
    # ex 9 ,8
    a, b = N * 9, N * 8
    print(f'#{tc}', a, b)
