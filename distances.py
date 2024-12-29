from collections import Counter

def distance_hamming(mot1,mot2):
    if len(mot1) == 0 or len(mot1) != len(mot2): return None

    distance = sum(1 for a, b in zip(mot1, mot2) if a != b)
    return distance

def distance_jaccard(mot1, mot2):
    # distance = 1 - nombre de lettre communes / nombre total de lettre

    tab_mot1 = decomposition_lettre(mot1)
    tab_mot2 = decomposition_lettre(mot2)

    min_tab = min(tab_mot1, tab_mot2)
    max_tab = max(tab_mot1, tab_mot2)
    
    lettre_commune = sum(1 for a in min_tab if a in max_tab)

    nb_lettres = count_letters(mot1, mot2, False)
    return 1 - (lettre_commune/len(nb_lettres))

def decomposition_lettre(mot, uniqueLetter=False):
    if len(mot) == 0: return None

    if uniqueLetter == True:
        return sorted(list(set(list(mot))))
    else:
        return sorted(list(mot))

def count_letters(mot1, mot2, uniqueLettre=False):
    compteur1 = Counter(mot1)
    compteur2 = Counter(mot2)

    compteur = compteur1 | compteur2

    # Tri par ordre alphabétique
    compteur = dict(sorted(compteur.items()))
    #print('Dictionnaire des lettres et fréquences :', compteur)

    result = []
    for lettre, count in compteur.items():
        result.extend([lettre] * count)
    return result

def distance_levenshtein(mot1, mot2):
    if len(mot1) == 0 or len(mot2) == 0: return None

    tab_mot1 = list(mot1)
    tab_mot2 = list(mot2)

    # Initialiasation
    M = [['', ''] + tab_mot2]
    M.append([''] + [a for a in range(len(tab_mot2) + 1)])
    for i in range(len(tab_mot1)+2):
        if (i > 1):
            M.append([tab_mot1[i-2], i-1] + ([''] * len(tab_mot2)))

    # récupérer les cases grisees
    grey_case = []
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i > 1 and j > 1 and M[i][0] == M[0][j]:
                grey_case.append((i,j))
    
    def find_grey(L, i,j):
        left = L[i][j-1] + 1
        up = L[i-1][j] + 1
        diag = L[i-1][j-1]
        return min(left, up, diag)
    
    def find_white(L, i,j):
        left = L[i][j-1] + 1
        up = L[i-1][j] + 1
        diag = L[i-1][j-1] + 1
        return min(left, up, diag)
    
    # remplir le tableau
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i > 1 and j > 1:
                if (i,j) in grey_case:
                    M[i][j] = find_grey(M, i, j)
                else:
                    M[i][j] = find_white(M, i, j)

    # distance de Levenshtein est la valeur de la case en bas à droite
    return M[len(M)-1][len(M[0])-1]