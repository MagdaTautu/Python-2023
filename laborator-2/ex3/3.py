def divide_with_remainders(a, b, nr_zecimale):

    cat, rest = divmod(a,b )
    
    zecimale = []

    for _ in range (nr_zecimale):
        a = rest * 10 #se adauga o noua zecimala in fata restului
        cat, rest = divmod(a, b)
        zecimale.append(str(cat))

    result = f"{cat}." + "".join(zecimale)
    return result


numarator = 22  
numitor = 7  
nr_zec = 100  

result = divide_with_remainders(numarator, numitor, nr_zec)
print(result)
