T = int(input())

my_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
           'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
           'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

for tc in range(1, T + 1):
    N = int(input())
    alpha = [0] * 26
    ans = 0
    for _ in range(N):
        title = input()
        alpha[my_dict[title[0]]] += 1

    for i in range(26):
        if alpha[i] != 0:
            ans += 1
        else:
            break
    print(f'#{tc} {ans}')
