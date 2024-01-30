alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Mystere(l):
    k = 0
    while k < 27:
        if l == alpha[k]:
            return k
        k = k+1

def cryptage(message):
    rep = ""
    for c in message:
        n = Mystere(c) + 2
        rep = rep + alpha[n%27]
    return rep

def decryptage(message):
    rep = ""
    for c in message:
        n = Mystere(c) - 2
        rep = rep + alpha[n%27]
    return rep
        

def cryptage2(message, decal):
    rep = ""
    for c in message:
        n = Mystere(c) + decal
        rep = rep + alpha[n%27]
    return rep

def decryptage2(message, decal):
    rep = ""
    for c in message:
        n = Mystere(c) - decal
        rep = rep + alpha[n%27]
    return rep
    
    
def compteLettre(message, chara):
    nbLettre = 0
    for c in message:
        if c == chara:
            nbLettre += 1
    return nbLettre
    
def lettreMax(message):
    nbMaxLettre = 0
    lettre = 0
    for i in range(0, len(alpha)):
        nbLettre = compteLettre(message, alpha[i])
        if nbLettre > nbMaxLettre:
            nbMaxLettre = nbLettre
            lettre = alpha[i]
    return lettre
            
            

def cryptage3(message, cle):
    rep = ""
    for c in range(len(message)):
        decal = Mystere(cle[c % len(cle)])
        n = Mystere(message[c]) + decal
        rep = rep + alpha[n%27]
    return rep
    
def decryptage3(message, cle):
    rep = ""
    for c in range(len(message)):
        decal = Mystere(cle[c % len(cle)])
        n = Mystere(message[c]) - decal
        rep = rep + alpha[n%27]
    return rep
    
    
    
def bruteForce3(message, longueurCle):
    # crée un tableau pour chaque lettre de la clé
    chaineParCaraCle = []
    
    dechiffre = []
    
    reponse = ""
    for t in range(longueurCle):
        chaineParCaraCle.append("")
        
        
    #ajoute les lettres dans leur tableau respectif
    for i in range(len(message)):
        chaineParCaraCle[i % longueurCle] = chaineParCaraCle[i % longueurCle] + message[i]
        
    #donne l'indice du charactère le plus présent pour chaque charactère de la clé
    for k in range(len(chaineParCaraCle)):
        indiceLettre = Mystere(lettreMax(chaineParCaraCle[k]))
        print(indiceLettre)
        dechiffre.append(decryptage2(chaineParCaraCle[k], indiceLettre))
        
    num = -1
    for j in range(len(message)):
        if j % longueurCle == 0:
            num += 1
        reponse = reponse + dechiffre[j%longueurCle][num]
        
        
    return reponse
            