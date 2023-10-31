def dict(string):
    d = {}
    for i in string:
        if i in d:
            d[i] += 1
        else: d[i] = 1
    return d

result = dict("Ana has apples.")
print(result)