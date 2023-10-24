def fibonacci(n):
    lista = []
    a, b = 0, 1
    for _ in range(n):
        lista.append(a)
        c=a
        a=b
        b=c+b
        #a, b = b, a + b
    print(lista)

fibonacci(10)
