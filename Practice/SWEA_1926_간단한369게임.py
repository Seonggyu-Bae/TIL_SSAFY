N = int(input())

for i in range(1, N + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9 or i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        while i != 0:
            if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
                print('-', end='')
            i //= 10
        print('', end=' ')
    else:
        print(i, end=' ')
