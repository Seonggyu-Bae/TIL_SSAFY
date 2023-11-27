T = int(input())

for tc in range(1, T + 1):
    count = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    my_str = input()

    for i in range(len(my_str)):
        if my_str[i] == alpha[i]:
            count += 1
        else:
            break

    print(f'#{tc} {count}')