def tuples(lista):
    a = len(set(lista))
    b = len(lista) - a
    return (a,b)
lista = [1, 2, 2, 3, 4, 4, 5, 5, 6]
result = tuples(lista)
print(result)