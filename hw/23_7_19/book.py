# book.py
number_of_book = 100

def decrease_book(rentalbooks_num):
    global number_of_book
    number_of_book -= rentalbooks_num
    print(f'남은 책의 수: {number_of_book}')
