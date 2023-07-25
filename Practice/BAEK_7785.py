import sys
input = sys.stdin.readline

N = int(input())
CIAO_log = {}
for i in range(N):
    name, log = input().split()
    CIAO_log.update({name : log})

log_list = sorted(list(CIAO_log.items()))

for i in range(len(log_list)-1,-1,-1):
    if log_list[i][1] == 'enter':
        print(log_list[i][0])