def add_item_to_dict(given_dict,add_key,add_value):
    new_dict = given_dict.copy()
    update_info = {add_key:add_value}
    new_dict.update(update_info)
    
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
