import os
import re

from utils import timedFunction, fileToSkip, rankResult, scoringUni, humanReadable
from utils import forbiddenDir, forbiddenTypes

# 5Mo
max_size = 5 * 1024 * 1024

#recuperer tous les dossiers d'un repertoire
def getDirFromRep(rep):
    return [os.listdir(rep)]

def getAllDirsFromRep(rep):
    dirs = []
    for root, dirs_in_root, _ in os.walk(rep):
        for dir_name in dirs_in_root:
            if dir_name not in forbiddenDir:
                dirs.append(os.path.join(root, dir_name))
    return dirs

# fonction pour rechercher un fichier en fonction de son nom
@timedFunction
def getFileFromName(name):
    result = []
    try:
        for root, dirs, files in os.walk('/'):
            dirs[:] = [d for d in dirs if d not in forbiddenDir]

            for file in files:
                if fileToSkip(name, file):
                    continue
                
                if file.lower() == name.lower():
                    result.append(os.path.join(root, file))
    except PermissionError:
        pass
    return result
#print(getFileFromName('main.py'))

# Recherche d'un mot-clé dans un fichier (lecture ligne par ligne pour économiser de la mémoire)
def search_in_file(file_path, keyword):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if keyword.lower() in line.lower():
                    return True
    except (IOError, PermissionError):
        pass  # Ignorer les fichiers qui ne peuvent pas être lus
    return False

# rechercher le nombre de fois ou le mot cle est present (nom du fichier + dans le fichier)
def search_in_file_with_rank(file_path, keyword):
    result = 0
    matches = []
    low_key = keyword.lower()

    try:

        file_size = os.path.getsize(file_path)

        def process_file(f):
            nonlocal matches
            nonlocal low_key
            if not humanReadable(f):  # Si le fichier n'est pas lisible, l'ignorer
                return 0

            # Lire tout le fichier ou ligne par ligne en fonction de la taille
            if file_size <= max_size:
                content = f.read().lower()  # Lire tout le fichier
                matches.extend(re.findall(r'\b' + re.escape(low_key) + r'\w*', content))
            else:
                for line in f:
                    low_line = line.lower()
                    matches.extend(re.findall(r'\b' + re.escape(low_key) + r'\w*', low_line))
        
        for word in os.path.basename(file_path).split():
            if os.path.basename(file_path).split('.') and (os.path.basename(file_path).split('.')[-1] in forbiddenTypes):
                return 0
            result += scoringUni(low_key, word)

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            process_file(f)

        #calculer score et classer
        for match in matches:
            result += scoringUni(low_key, match)

    except (IOError, PermissionError, UnicodeDecodeError):
        return result

    return result

# fonction pour rechercher un fichier en fonction d'un mot clé dans le fichier
@timedFunction
def getFileFromKeyWord(keyword):
    result = []
    try:
        for root, dirs, files in os.walk('/'):
            dirs[:] = [d for d in dirs if d not in forbiddenDir]

            for file in files:
                if search_in_file(os.path.join(root, file), keyword):
                    result.append(os.path.join(root, file))
                
    except PermissionError:
        pass
    return result
#print(getFileFromKeyWord('timedFunction'))

# fonction pour rechercher avec ranking
@timedFunction
def getFileFromKeyWordWithRank(keyword):
    result = []
    try:
        for root, dirs, files in os.walk('/'):
            dirs[:] = [
                d for d in dirs
                if not any(forbidden in os.path.join(root, d) for forbidden in forbiddenDir)
            ]

            for file in files:
                count = search_in_file_with_rank(os.path.join(root, file), keyword)
                if count > 1:
                    result.append((os.path.join(root, file), count))
    except PermissionError:
        pass

    return rankResult(result), len(result)
print(getFileFromKeyWordWithRank('rank'))