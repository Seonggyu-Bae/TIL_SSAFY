T = int(input())

for tc in range(1, T+1):
    mem_value = input()
    mem_len = len(mem_value)
    init_mem = ['0'] * mem_len
    count = 0

    for i in range(mem_len):
        if init_mem[i] != mem_value[i]:
            v = mem_value[i]
            count += 1
            for j in range(i, mem_len):
                init_mem[j] = v

    print(f'#{tc} {count}')
