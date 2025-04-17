with open(r'C:\Users\Etudiant\Desktop\gitub48\cryptographie\message5.txt', 'r', encoding="utf-8") as file:
    message = file.read()
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
n=3
def decodage(text,clé):
    cheval = ''
    n = len(clé)
    for i in range(len(text)): 
        zebre = ord(text[i])
        zebre = zebre - clé[i % n]
        if zebre < 0:
            return 'ERREUR'
        cheval += chr(zebre)
    return cheval
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
print(n,texte)