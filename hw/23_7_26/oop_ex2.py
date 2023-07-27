import random
#로또 번호 생성 프로그램 작성
#1. 로또 번호 만드는 거
#2. 정렬

class LottoNumberMaker:

    def __init__(self):
        self.lotto_nums = []

    def create_number(self):
        while len(self.lotto_nums) < 6:
            ran_num = random.randint(1,45)
            if ran_num in self.lotto_nums:
                continue
            else:    
                self.lotto_nums.append(random.randint(1,45))

    def lotto_sort(self):
        self.lotto_nums.sort()


line1 = LottoNumberMaker()

line1.create_number()
line1.lotto_sort()
print(line1.lotto_nums)