# main.py

# 아래 함수를 수정하시오.
def count_character(my_string, find_char):
    count = 0
    for i in range(len(my_string)):
        if my_string[i] == find_char:
            count += 1
        else:
            pass
    return count

result = count_character("Hello, World!", "o")
print(result) # 2
