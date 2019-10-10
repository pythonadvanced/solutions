
##################################################
# comptage
##################################################
def comptage(in_filename, out_filename):
    """
    retranscrit le fichier in_filename dans le fichier out_filename
    en ajoutant des annotations sur les nombres de lignes, de mots
    et de caractères
    """
    # on ouvre le fichier d'entrée en lecture
    with open(in_filename, encoding='utf-8') as in_file:
        # on ouvre la sortie en écriture
        with open(out_filename, 'w', encoding='utf-8') as out_file:
            lineno = 1
            # pour toutes les lignes du fichier d'entrée
            # le numéro de ligne commence à 1
            for line in in_file:
                # autant de mots que d'éléments dans split()
                nb_words = len(line.split())
                # autant de caractères que d'éléments dans la ligne
                nb_chars = len(line)
                # on écrit la ligne de sortie; pas besoin
                # de newline (\n) car line en a déjà un
                out_file.write(f"{lineno}:{nb_words}:{nb_chars}:{line}")
                lineno += 1


##################################################
# comptage (bis)
##################################################
def comptage_bis(in_filename, out_filename):
    """
    un peu plus pythonique avec enumerate
    """
    with open(in_filename, encoding='utf-8') as in_file:
        with open(out_filename, 'w', encoding='utf-8') as out_file:
            # enumerate(.., 1) pour commencer avec une ligne
            # numérotée 1 et pas 0
            for lineno, line in enumerate(in_file, 1):
                # une astuce : si on met deux chaines
                # collées comme ceci elle sont concaténées
                # et on n'a pas besoin de mettre de backslash
                # puisqu'on est dans des parenthèses
                out_file.write(f"{lineno}:{len(line.split())}:"
                               f"{len(line)}:{line}")


##################################################
# comptage (ter)
##################################################
def comptage_ter(in_filename, out_filename):
    """
    pareil mais avec un seul with
    """
    with open(in_filename, encoding='utf-8') as in_file, \
         open(out_filename, 'w', encoding='utf-8') as out_file:
        for lineno, line in enumerate(in_file, 1):
            out_file.write(f"{lineno}:{len(line.split())}:"
                           f"{len(line)}:{line}")

