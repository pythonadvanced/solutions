# le problème des tours est équivalent
# à celui qui consiste à énumérer
# toutes les permutations
def rooks(n):
    
    if n == 1 :
        yield [1]
        # on en a terminé, il faut sortir de rooks()
        # (on aurait pu aussi mettre un else)
        return
    
    for smaller in rooks(n-1):
        # si on trouve par exemple n=4
        # on balaie S3 et pour par exemple la permutation
        # smaller=[3, 2, 1]
        # on va énumérer dans S4 les 4 permutations
        # i=0 -> [3, 2, 1, 4]   
        # i=1 -> [3, 2, 4, 1]
        # i=2 -> [3, 4, 2, 1]
        # i=3 -> [4, 3, 2, 1]
        for i in range(n):
            yield smaller[i:] + [n] + smaller[:i]    

# pour les reines
# pour vérifier si une configuration est valide 
# on remarque qu'une diagonale donnée a une équation, selon le sens
# x + y = constante 
# x - y = constante    
# donc pour que les 8 points soient tous sur des diagonales différentes
# il faut et il suffit que leurs (x+y) (resp. x-y) soient tous différents
# on va donc calculer l'ensemble de leurs (x+y) 
# qui doit être de cardinal n
def queens_ok(L, n):
    return (
        len({x+y for (x, y) in enumerate(L)}) == n
        and
        len({x-y for (x, y) in enumerate(L)}) == n
    )


def queens(n):
    # on doit passer à filter une fonction, mais qui dépend de n
    # on crée donc une clôture
    return filter(lambda L: queens_ok(L, n), rooks(n))


# ---- 
# question subsidiaire
# comment calculeriez-vous le nombre de solutions
# sachant qu'on ne peut pas appeler len() sur un générateur 

# ----    
def test_rooks(n):
    print(f"==== rooks({n})")
    for solution in rooks(n):
        print(solution)
    total = sum(map(bool, rooks(n)))
    unique = len(set(tuple(L) for L in rooks(n)))
    print(f"found a total of {total}")
    print(f"unique: {unique}")
    assert total == unique
    

def test_queens(n):
    total = sum(map(bool, queens(n)))
    print(f"==== {total} solutions for queens({n})")
    for i, solution in enumerate(queens(n)):
        if i >= 6:
            print("...")
            break
        print(solution)
    if n == 8:
        assert total == 92
        
        
if __name__ == '__main__':
    test_rooks(4)
    test_queens(6)
    test_queens(8)
    