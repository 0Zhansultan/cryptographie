import math
with open('message6.txt', 'r', encoding="utf-8") as file:
    message = file.read()

def trouver_taille_cle(texte):
    sequences = {}
    distances = []

    for i in range(len(texte)-5):
        sequence = texte[i:i+5]
        if sequence in sequences:
            distance = i - sequences[sequence]
            distances.append(distance)
            if len(distances) >= 2:  
                break
        else:
            sequences[sequence] = i

    if len(distances) >= 2:
        return math.gcd(distances[0], distances[1])
    return 3  

def analysefreqcar(message):
    dico = {}
    for i in message:
        if i in dico:
            dico[i] += 1
        else:
            dico[i] = 1
    return dico

def plus_freq(dico):
    most_frequent_char = max(dico, key=dico.get)
    return most_frequent_char, dico[most_frequent_char]

def decodage(text, cle):
    cheval = ''
    n = len(cle)
    for i in range(len(text)):
        zebre = ord(text[i])
        zebre = zebre - cle[i % n]
        if zebre < 0:
            zebre += 128 
        cheval += chr(zebre)
    return cheval

n = trouver_taille_cle(message)
print(f"Taille de clé détectée : {n}")

morceaux = ['' for i in range(n)]
freq = [{} for i in range(n)]
cle = [0 for i in range(n)]
plusfrequent_char = ['' for i in range(n)]
frequency = [0 for i in range(n)]

for i in range(n):
    morceaux[i] = message[i::n]
    freq[i] = analysefreqcar(morceaux[i])
    plusfrequent_char[i], frequency[i] = plus_freq(freq[i])
    cle[i] = ord(plusfrequent_char[i]) - ord(' ')

texte = decodage(message, cle)
print(texte)