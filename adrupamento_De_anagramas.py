# buscando dentro das collections de python o defaultdict para ditar

from collections import defaultdict

# Definindo grupo de anagramas

def grupo_anagrama(a):
    # Aqui foi definido que a variavel que recebe o defaultdict que pode ser chamado de df foi definido como uma lista
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()
# Codigo feito baseado no exemplo pois achei mais didático
palavras = ["tea", "eat", "bat", "ate", "arc", "car"]
print(grupo_anagrama(palavras))
