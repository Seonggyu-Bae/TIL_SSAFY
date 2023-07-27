import random
#로또 번호 생성 프로그램

lotto_nums = [] #생성된 로또 번호를 저장

#랜덤으로 로또 번호를 생성

while len(lotto_nums) < 6 :
    ran_num = random.randint(1,45)
    if ran_num in lotto_nums:
        continue
    else:    
        lotto_nums.append(random.randint(1,45))

print(lotto_nums)