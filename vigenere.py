
##################################################
# vigenere
##################################################
from itertools import cycle

# grâce à une combinaison de zip et de itertools.cycle
# on peut itérer sur
# d'une part, le message
# et d'autre part, sur la clé, en boucle
#
# notez que
# (*) cycle ne s'arrête jamais
# (*) mais zip, lui, s'arrête au plus court de ses (ici deux)
#     ingrédients
# ce qui fait que zip(message, cycle(cle))
# fait exactement ce dont on a besoin

def vigenere(clear, key, encode=True):
    return "".join(
        cesar(c, k, encode)
        for c, k in zip(clear, cycle(key))
    )

