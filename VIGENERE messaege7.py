import math
with open('message7.txt', 'r', encoding="utf-8") as file:
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
        taille = math.gcd(distances[0], distances[1])
        print(taille)  
        return taille
    return 3

def analysefreqcar(texte):
    dico = {}
    for j in texte:
        if j in dico:
            dico[j] += 1
        else:
            dico[j] = 1

    a = 0
    most = ''
    for k in dico:
        if dico[k] > a:
            a = dico[k]
            most = k

    return ord(most) - ord(' ')  

def decodage_cesar_auto(texte):
    cle = trouver_taille_cle(texte)

    groupes = ['' for _ in range(cle)]
    for i in range(0, len(texte) - cle, cle):
        for j in range(cle):
            groupes[j] += texte[i + j]

    groupes_dechiffres = ['' for _ in range(cle)]
    for x in range(cle):
        decalage = analysefreqcar(groupes[x])
        for h in range(len(groupes[x])):
            num = ord(groupes[x][h])
            groupes_dechiffres[x] += chr(num - decalage)

    decode = ''
    for i in range(len(texte)//cle):
        for m in range(cle):
            if i < len(groupes_dechiffres[m]):
                decode += groupes_dechiffres[m][i]

    return decode
message_dechiffre = decodage_cesar_auto(message)
print(message_dechiffre)