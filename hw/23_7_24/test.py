"""def count_character(my_string, find_char):
    return my_string.count(find_char)

result = count_character("Hello, World!", "o")
print(result) # 2
"""


def count_character(my_string, find_char):
    count = 0
    if find_char in my_string:
        print('??')
    else:
        pass
    return count

result = count_character("Hello, Worlld!", "ll")
print(result) # 2
