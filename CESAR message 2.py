#%%
with open(r'C:\Users\Etudiant\Desktop\gitub48\cryptographie\message2.txt', 'r', encoding="utf-8") as file:
    message = file.read()

def decodage(text,clé):
    cheval=''
    for i in range(len(text)):
        zebre= ord(text[i])
        zebre=zebre-clé
        cheval+=chr(zebre)
    return cheval

cle=0
texte=decodage(message, cle)
while  ' est ' not in texte:
    cle+=1
    texte=decodage(message, cle)
print(cle)
print(texte)
# %%
