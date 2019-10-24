
##################################################
# alternat
##################################################
def alternat(iter1, iter2):
    """
    renvoie une liste des éléments
    pris alternativement dans iter1 et dans iter2
    """
    # pour réaliser l'alternance on peut combiner zip avec aplatir
    # telle qu'on vient de la réaliser
    return aplatir(zip(iter1, iter2))


##################################################
# alternat_bis
##################################################
def alternat_bis(iter1, iter2):
    """
    une deuxième version de alternat
    """
    # la même idée mais directement, sans utiliser aplatir
    return [element for conteneur in zip(iter1, iter2)
            for element in conteneur]

