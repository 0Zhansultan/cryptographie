#%%
with open(r'C:\Users\Etudiant\Desktop\gitub48\cryptographie\message3.txt', 'r', encoding="utf-8") as file:
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

def decodage(text, clé):
    cheval = ''
    for i in range(len(text)):
        zebre = ord(text[i])
        zebre = zebre - clé
        cheval += chr(zebre)
    return cheval

freq = analysefreqcar(message)
plusfrequent_char, frequency = plus_freq(freq)
print(f"Le caractère le plus fréquent est '{plusfrequent_char}' avec {frequency} apparitions.")

cle = ord(plusfrequent_char) - ord(' ')
print(f"La clé de décalage calculée est {cle}")

texte = decodage(message, cle)
print("Message décodé :")
print(texte)