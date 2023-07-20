list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

#list comprehension을 사용한 list_of_book에 없는 rental_book을 missing_book에 할당
missing_book = [book for book in rental_book if not(book in list_of_book)]

exist = 0
all_exist = 1
k = 0
for i,r_book in enumerate(rental_book):

    for j,l_book in enumerate(list_of_book):
        if r_book == l_book:
            exist = 1

    if exist == 0 and j==len(list_of_book)-1:
        all_exist=0
        print(f'{r_book} 을/를 보충하여아 합니다.')

    if exist == 1 and all_exist == 1 and i == len(rental_book)-1 and j == len(list_of_book)-1:
        print('모든 도서가 대여 가능한 상태입니다.')

    exist = 0    
