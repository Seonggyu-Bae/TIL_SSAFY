# ws_5_4.py

# 아래 함수를 수정하시오.
def capitalize_words(my_word):
    new_word = list(my_word)
    i = 0
    for idx,my_char in enumerate(new_word):
        if idx == 0:
            new_word[idx] = new_word[idx].upper()
        if i == 1:
            new_word[idx] = new_word[idx].upper()
            i=0
        if my_char == ' ':
            i=1

    return ''.join(new_word)

result = capitalize_words("hello, world!")
print(result)
