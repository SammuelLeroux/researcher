def distance_hamming(mot1,mot2):
    if len(mot1) == 0 or len(mot2) == 0: return 0

    result = 0
    count = 0
    for word_mot1 in mot1:
        if word_mot1 != mot2[count]:
            result += 1
        count += 1
    return result