def merge_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    result = [tuple(lst[i] if i < len(lst) else None for lst in lists) for i in range(max_length)]
    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b"]

result = merge_lists(list1, list2, list3)
print(result)
