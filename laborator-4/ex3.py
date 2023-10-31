def recursive_dict_compare(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        value1, value2 = dict1[key], dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict): #verific daca ambele chei sunt dictionare
            if recursive_dict_compare(value1, value2) == False:
                return False
        else:
            if value1 != value2:
                return False

    return True

dict1 = {'a': 1, 'b': {'c': 2, 'f': [3, 4]}, 'e': [5, 6]}
dict2 = {'a': 1, 'b': {'c': 2, 'f': [3, 4]}, 'e': [5, 6]}

result = recursive_dict_compare(dict1, dict2)
print(result)  
