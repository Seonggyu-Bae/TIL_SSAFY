def difference_sets(*my_sets):
    diff_set = set
    for my_set in my_sets:
        diff_set = diff_set.difference(my_set)
    return diff_set

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)