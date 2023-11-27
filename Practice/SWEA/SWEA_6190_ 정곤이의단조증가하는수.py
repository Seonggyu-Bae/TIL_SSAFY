T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    danjo_max = -1          # 단조 증가하는 수가 없다면 -1을 출력해야함

    for i in range(N):
        for j in range(i + 1, N):   # 1 <= i < j <= N 임으로 j의 시작점은 i보다 커야함
            multi = A[i] * A[j]
            if multi < danjo_max:   # 이전에 찾은 단조값 보다 작으면 계산할 필요없음
                continue
            multi_str = str(multi)      # 각 자리수를 비교하기 위해 문자열로 변환
            multi_len = len(multi_str)
            is_danjo = True             # 단조인지 아닌지 확인을 위한 변수
            for k in range(1, multi_len):
                if multi_str[k] < multi_str[k - 1]: # 현재자리보다 앞자리가 크면 단조가 아님
                    is_danjo = False
                    break
            if is_danjo and multi > danjo_max:
                danjo_max = multi

    print(f'#{tc} {danjo_max}')
