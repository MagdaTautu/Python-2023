def find_x(x,*liste):
   
    lista  = [element for lista in liste for element in lista]
    print(lista)
    rezultat = []
    count = 0 
    for el in lista:
        n = lista.count(el)
        if n == x and el not in rezultat:
            rezultat.append(el)
    return rezultat

lista1 = [1,2,3]
lista2 = [2,3,4] 
lista3 = [4,5,6]
lista4 = [4,1, "test"]
x=2
result = find_x(x, lista1, lista2, lista3, lista4)
print(result)
