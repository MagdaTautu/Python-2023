numere = [0, 1, 2, 3, 4]

secventa = ""
n0 = 0
n1 = 0

for numar in numere:
    secventa_binara = format(numar, '08b') 
    secventa += secventa_binara + " "
    n0 += secventa_binara.count('0')
    n1 += secventa_binara.count('1')
print(secventa)
print(n0,n1)
