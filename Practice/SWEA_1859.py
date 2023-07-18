T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sum = 0
    high = 0
    N = int(input())
    day_cost = list(map(int, input().split()))
    day_cost_max = max((day_cost))

    print(day_cost_max)
    for i in range(N):

        sum += high
        high = 0
        
        for j in range(i,N):
            x = day_cost[j] - day_cost[i]
            if x > high:
                high = x

    print(f'#{test_case} {sum}')