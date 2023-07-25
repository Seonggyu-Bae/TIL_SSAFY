import sys
#sys.stdin.readline()

N,M = map(int, input().split())

pocketmon = {}
pocketmon_1 = {}

for i in range(N):
    temp = sys.stdin.readline().rstrip()
    pocketmon.update({temp : i})            #디지몬 이름 나왔을때 몇번째인지 출력을위해
    pocketmon_1.update({i : temp})          #몇번째 인지 나왔을때 디지몬 이름을 출력하기 위해

for i in range(M):
    x = sys.stdin.readline().rstrip()
    if x.isdecimal():
        print(pocketmon_1.get(int(x)-1))
    else:
        print(pocketmon.get(x)+1)