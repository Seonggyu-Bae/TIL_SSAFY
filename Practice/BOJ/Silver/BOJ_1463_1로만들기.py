def solve(num, cnt):
    global ans
    if cnt > ans:
        return
    if num == 1:
        if cnt < ans:
            ans = cnt
        return
    if num % 3 == 0:
        solve(num // 3, cnt + 1)
    if num % 2 == 0:
        solve(num // 2, cnt + 1)
    solve(num - 1, cnt + 1)


N = int(input())
ans = 0xfffffff

solve(N,0)

print(ans)