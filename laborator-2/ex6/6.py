import itertools

def gen_permutari(alphabet, p):
    permutari = list(itertools.permutations(alphabet, p))
    words = [''.join(permutare) for permutare in permutari]
    return words

alphabet = "abc"
p = 2

permutari = gen_permutari(alphabet, p)
for cuvant in permutari:
    print(cuvant)