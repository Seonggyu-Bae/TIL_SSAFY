N, K = map(int, input().split())

temp = [x for x in range(1,N+1)]
yo = []
count = 0

while temp:
    count  = (count + K - 1) % len(temp)
    yo.append(temp.pop(count))
    
print('<' + ', ' .join(map(str,yo)) + '>')