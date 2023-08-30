"""
아이스크림 가게에는 N종류의 아이스크림이 있다.
모든 아이스크림은 1부터 N까지 번호가 매겨져있다.
어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다.
따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다.
이때, 선택하는 방법이 몇 가지인지 구하려고 한다.

첫째 줄에 정수 N과 M이 주어진다.
N은 아이스크림 종류의 수이고,
M은 섞어먹으면 안 되는 조합의 개수이다.
아래 M개의 줄에는 섞어먹으면 안 되는 조합의 번호가 주어진다.
같은 조합은 두 번 이상 나오지 않는다. (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)
"""
import sys

def comb(N, K, idx, cnt):  # N개중에 K개를 고를거임
    if cnt == K:
        temp = []
        for i in range(N):
            if selected[i]:
                temp.append(i+1)
        c.append(temp[:])
        return
    if idx == N:
        return

    selected[idx] = 1
    comb(N, K, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(N, K, idx + 1, cnt)


N, M = map(int, sys.stdin.readline().split())

no = []
c = []
selected = [0] * N
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    no.append([a, b])

comb(N, 3, 0, 0)
count = len(c)

for i in range(len(c)):
    for j in range(M):
        t_cnt = 0
        for k in no[j]:
            if k in c[i]:
                t_cnt += 1
        if t_cnt == len(no[j]):
            count -= 1
            break

print(count)

