def intersection_sets(*my_sets):
    inter_set = set

    for my_set in my_sets:
        inter_set = inter_set.intersection(my_set)

    return inter_set
    

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result) # {3}