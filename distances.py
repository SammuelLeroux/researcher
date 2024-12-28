def distance_hamming(mot1,mot2):
    if len(mot1) == 0 or len(mot1) != len(mot2): return None

    distance = sum(1 for a, b in zip(mot1, mot2) if a != b)
    return distance

def distance_jaccard(mot1, mot2):
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
    result = decomposition_lettre(mot1, uniqueLettre)
    tab_mot2 = decomposition_lettre(mot2, uniqueLettre)

    for mot in tab_mot2:
        if not mot in result:
            result.append(mot)
        
    return sorted(result)
