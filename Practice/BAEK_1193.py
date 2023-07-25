X = int(input())

line_num = 0  # 사선 라인
max_num = 0  # 입력된 숫자(X)의 라인에서 가장 높은 순서
while X > max_num:
    line_num += 1  
    max_num += line_num  


gap = max_num - X  #같은 라인의 가장 높은 순서와의 차이 계산

if line_num % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line_num - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line_num - gap  #분모
    
print(f'{top}/{under}')