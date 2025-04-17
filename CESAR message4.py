#%%
with open(r'C:\Users\Etudiant\Desktop\gitub48\cryptographie\message4.txt', 'r', encoding="utf-8") as file:
    message = file.read()

def dechiffrer_cesar_double(message):
    pairs = message[0::2]
    impairs = message[1::2]

    def plus_frequent(texte):
        return max(set(texte), key=texte.count)

    freq_pair = plus_frequent(pairs)
    freq_impair = plus_frequent(impairs)

    cle_pair = ord(freq_pair) - ord(' ')
    cle_impair = ord(freq_impair) - ord(' ')

    message_dechiffre = []
    for i in range(len(message)):
        if i % 2 == 0:
            message_dechiffre.append(chr(ord(message[i]) - cle_pair))
        else:
            message_dechiffre.append(chr(ord(message[i]) - cle_impair))
    return ''.join(message_dechiffre), cle_pair, cle_impair

texte, cle_pair, cle_impair = dechiffrer_cesar_double(message)
print("Clé paire :", cle_pair, "Clé impaire :", cle_impair)
print("Message déchiffré :")
print(texte)
# %%
