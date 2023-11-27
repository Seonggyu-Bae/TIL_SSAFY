import sys

def solve(day, earn):
    global ans

    if day == N:
        if earn > ans:
            ans = earn
        return

    if day + TandP[day][0] <= N:
        solve(day + TandP[day][0], earn + TandP[day][1])
        solve(day + 1, earn)
    else:
        solve(day + 1, earn)


N = int(input())

TandP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
solve(0, 0)
print(ans)
