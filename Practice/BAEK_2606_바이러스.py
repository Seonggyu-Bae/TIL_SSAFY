def my_bfs(start, v):
    global count
    visited = [0] * (v + 1)
    visited[start] = 1
    Q = [start]

    while Q:
        current = Q.pop(0)
        count += 1
        for i in range(1, v + 1):
            if connect_info[current][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = 1
    return count


pc = int(input())
connect_line_num = int(input())

connect_info = [list([0] * (pc + 1)) for _ in range(pc + 1)]

for _ in range(connect_line_num):
    s, e = map(int, input().split())
    connect_info[s][e], connect_info[e][s] = 1, 1

count = -1  # 처음 웜바이러스에 걸린 컴퓨터는 제외하기위해 초기값을 -1로 설정함

print(my_bfs(1, pc))
