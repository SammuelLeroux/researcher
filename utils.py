import time

forbiddenDir = ["site-packages", "tmp", "var", ".git", "sdk", "node_modules", "vendor", "__pycache__", ".npm", ".cache", "bin", "build", "_build", "dist", "x86_64", "debug", ".config", ".gradle", ".svn", ".idea", ".vscode", ".DS_Store", "Thums.db", "proc", 'sys', "dev", "System32", "caches", "cache", "snap"]
forbiddenTypes = ["sav", "vdi", "sst", "bin", "dill", "exe", "dll", "so", "out", "class", "apk", "mp4", "mp3", "avi", "mov", "wav", "iso", "img", "dmg", "filecache", "class", "jar", "lib"]

def timedFunction(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Enregistre l'heure de début
        result = func(*args, **kwargs)  # Exécute la fonction
        end_time = time.time()  # Enregistre l'heure de fin
        execution_time = end_time - start_time  # Calcule le temps d'exécution
        print(f"Temps d'exécution de {func.__name__}: {execution_time:.4f} secondes")
        return result  # Renvoie le résultat de la fonction
    return wrapper

def fileToSkip(lookingFor, file):
    if lookingFor.split(".")[-1] in forbiddenTypes: return True

    # si on recherche un fichier en fonction du nom et que on met un type, on peut skip ceux qui ne sont pas du meme type
    if lookingFor.split(".")[-1] == file.split(".")[-1]:
        return False
    
    return True

def rankResult(results):
    # Trie les résultats par nombre d'occurrences décroissant
    return sorted(results, key=lambda x: x[1], reverse=True)

# scoring pour un keyword d'un seul mot
def scoringUni(keyword, match):
    result = 0
    if keyword.lower() == match.lower():
        result += 1  # Occurrence exacte du mot
    elif keyword.lower() in match.lower():
        result += 1/(len(match) - len(keyword) + 1)  # Occurrence partielle du mot, divisé par le nombre de mots en plus
    
    return result

def humanReadable(file):
    """Fonction pour vérifier si un fichier est lisible par un humain (texte)"""
    try:
        content = file.read(1024)  # Lire un petit morceau du fichier
        # Vérifier si tout le contenu est imprimable et ne contient pas de caractères binaires
        if all(c.isprintable() or c.isspace() for c in content):
            return True
        return False
    except Exception as e:
        # Si une exception survient, on considère le fichier comme illisible
        return False

# scoring pour un keyword de plusieurs mots