def is_palindrome(string):
    last_2 = string[-2::1] # slice operator = start : end : pas
    return last_2

def group_by_rhyme(words):
    # Create a dictionary to store words grouped by their last two letters
    rhymes  = {}
    
    for word in words:
        last_2 = word[-2::1]
        
        if last_2 in rhymes:
            rhymes[last_2].append(word)
        else:
            rhymes[last_2] = [word]

    
    grouped_lists = list(rhymes.values())
    
    return grouped_lists

word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(word_list)
print(result)
