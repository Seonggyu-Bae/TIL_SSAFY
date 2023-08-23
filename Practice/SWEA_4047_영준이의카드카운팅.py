T = int(input())

for tc in range(1, T + 1):
    S, D, H, C = [0] * 14, [0] * 14, [0] * 14, [0] * 14 # 카드정보저장할배열
    S_C, D_C, H_C, C_C = 13, 13, 13, 13                 # 카드 갯수

    card_info = input()
    info_len = len(card_info)
    is_valid = True                                     # 겹치는 카드가 있다면 오류를 출력하기 위하 만든 변수

    for i in range(0, info_len, 3):                     # 카드 정보가 3자리로 표현됨
        if not is_valid:                                # 겹치는 카드가 있으면
            break                                       # 종료

        if card_info[i] == 'S':
            card_num = int(card_info[i + 1:i + 3])      # 카드 숫자를 읽음
            if S[card_num] != 0:                        # 카드정보저장배열에 이미 있는 카드라면(겹치는 카드라면)
                is_valid = False                        # 오류 출력을 위해 만든 변수를 바꿔주고
                break                                   # 종료
            else:
                S[card_num] += 1                        # 카드정보를 저장
                S_C -= 1                                # 카드개수를 하나 빼줌

        elif card_info[i] == 'D':
            card_num = int(card_info[i + 1:i + 3])
            if D[card_num] != 0:
                is_valid = False
                break
            else:
                D[card_num] += 1
                D_C -= 1

        elif card_info[i] == 'H':
            card_num = int(card_info[i + 1:i + 3])
            if H[card_num] != 0:
                is_valid = False
                break
            else:
                H[card_num] += 1
                H_C -= 1

        else:  # C
            card_num = int(card_info[i + 1:i + 3])
            if C[card_num] != 0:
                is_valid = False
                break
            else:
                C[card_num] += 1
                C_C -= 1

    if is_valid:
        print(f'#{tc}', S_C, D_C, H_C, C_C)
    else:
        print(f'#{tc} ERROR')
