T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    total_sum = 0
    N = int(input())
    day_cost = list(map(int, input().split()))
    expensive = day_cost[N-1]

    #뒤에서 부터 도는 코드를 짜야 시간안에 돌듯?
    for j in range (N-2,-1,-1):
        if day_cost[j] < expensive:
            total_sum += expensive - day_cost[j]
        else:
            expensive = day_cost[j]
   
    print(f'#{test_case} {total_sum}')