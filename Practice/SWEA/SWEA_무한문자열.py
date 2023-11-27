def check(s1, s2):
    temp = len(s1) * len(s2)

    if len(s1) < temp:
        s1 *= temp // len(s1)
    if len(s2) < temp:
        s2 *= temp // len(s2)

    if s1 == s2:
        return True
    else:
        return False


T = int(input())

for tc in range(1, T + 1):
    str1, str2 = input().split()

    if check(str1, str2):
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')
