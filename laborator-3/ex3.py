def intersection(a, b):
    c = []
    c = [value for value in a if value in b]
    return c
def reunion(a,b):
    c = []
    c = sorted(list(set(a)) + list(set(b)))
    return c
def minus(a,b):
    c = []
    for element in a:
        if element not in b:
            c.append(element)
    return c

