def get_value_from_dict(m_dict, m_keys):

    return m_dict.get(m_keys)
    
my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice
