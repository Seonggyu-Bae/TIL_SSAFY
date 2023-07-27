import sys
from collections import Counter

N = int(input())

sang_card = sys.stdin.readline().split()

M = int(input())
find_card = sys.stdin.readline().split()

#counter 클래스는 시퀀스에서 각 요소가 몇 번 등장했는지 딕셔너리로 저장함
count = Counter(sang_card)

for i in range(len(find_card)):
    if find_card[i] in count:
        print(count[find_card[i]],end=' ')
    else:
        print(0,end=' ')          