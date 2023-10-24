def prim(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        i=i+1
    return True

def func(lista):
    nr_prime = [num for num in lista if prim(num)]
    return prime_list

lista = [2, 3, 4, 5, 6, 7, 8, 9, 10]
nr_prime = func(lista)
print(nr_prime)