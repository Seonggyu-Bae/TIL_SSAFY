def check_number():

    try:
        num = int(input('숫자를 입력하세요: '))
        temp = 100/num
        if num > 0:
            print('양수입니다.')
        else:
            print('음수입니다.')
    except ZeroDivisionError:   
            print('0입니다.')      
    except ValueError:
       print('잘못된 입력입니다.')
     
check_number()