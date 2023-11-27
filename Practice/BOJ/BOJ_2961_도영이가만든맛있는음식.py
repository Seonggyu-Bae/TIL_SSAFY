N = int(input())

food = [None] * N
sin = 0
sseun = 1
# 그 음식의 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.
for i in range(N):
    s, S = map(int, input().split())
    food[i] = [s, S]

