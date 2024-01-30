'''
#exo6
nom = input("quel est ton nom ")
print("Bonjour à toi ",nom)
'''
'''
#exo 7
distKm = float(input("quelle est la distance en km : "))
print(distKm," km correspondent à ", distKm/1.609, "miles")
'''
'''
#exo 8
nbGrenoille = int(input("nombre de grenoille : "))
nbCorbeau = int(input("nombre de corbeau : "))
nbRenard = int(input("nombre de renard : "))
tetes = nbGrenoille + nbCorbeau + nbRenard
pattes = nbGrenoille*4 + nbCorbeau*2 + nbRenard*4
queues = nbRenard
print("Il y a : ", tetes, " tete, ", pattes, " pattes, ", queues, " queues")
'''
'''
#exo9
tempF = float(input("Température en F : "))
print("La température est de : ", 5/9*(tempF-32), "°C")
'''
'''
#exo10
def secToDay():
    nbSec = int(input("Nombre de seconds : "))
    nbjour = nbSec//86400
    nbSec = nbSec-(nbjour*86400)
    nbHeure = nbSec//3600
    nbSec = nbSec-(nbHeure*3600)
    nbMin = nbSec//60
    nbSec = nbSec-(nbMin*60)
    if nbjour > 0 :
        print(nbjour," jours ", nbHeure, " heures ", nbMin, " minutes ", nbSec, " second")
    elif nbHeure > 0 :
        print(nbHeure, " heures ", nbMin, " minutes ", nbSec, " second")
    elif nbMin > 0 :
        print(nbMin, " minutes ", nbSec, " second")
    else :
        if nbSec > 1 :
            print(nbSec, " seconds")
        else :
            print(nbSec, " second")
    return
'''
'''
def nombre(nb) :
    if nb > 0 :
        return "le nombre est positif"
    elif nb == 0 :
        return "le nombre est nul"
    else :
        return "le nombre de est negatif"


def gameNumber():
    if a != 2:
        return "c'est gagné !"
    else :
        return "perdu"
    
def pair(nb):
    if nb%2 :
        return "pair"
    else :
        return "impair"

def supat0(nb) :
    if (nb<2 and nb>0):
        return "vrai"
    else :
        return "false"

def catSport(age):
    if 6<=age<=7 :
        return "poussin"
    elif 8<=age<=9 :
        return "pupille"
    elif 10<=age<=11 :
        return "minime"
    elif 6>age :
        return "error"
    else:
        return "cadet"
    
def annee(annee):
    return (((annee%4)== 0 and (annee%100)!= 0) or (annee%400)== 0)


def magasin(jour, heure):
    if ((jour <= 5 and (heure >=9 and heure <= 16)) or ((jour == 6 or jour == 7) and (heure >= 10 and heure <= 12))) :
        return "magasin ouvers"
    else :
        return "magasin fermé"
    
def oeufs(nbOeuf):
    douze = nbOeuf // 12
    reste = nbOeuf % 12
    six = reste // 6
    if ((reste % 6) != 0):
        six = six + 1
        
    print ("On utilise ", douze, "boites de 12 oeufs")
    print ("On utilise ", six, "boites de 6 oeufs")
    return
    
def photocopies(nbPhoto):
    prix1=0
    prix2=0
    prix3=0
    quantite=10
    quantite2=0
    quantite3=0
    if (nbPhoto > 30 ):
        prix1 = quantite * 0.1
        quantite2 = 20
        prix2 = quantite2 * 0.09
        quantite3 = nbPhoto-30
        prix3 = quantite * 0.08
        prixTTC = prix1 + prix2 + prix3
    elif (nbPhoto > 10):
        prix1 = quantite * 0.1
        quantite2 = nbPhoto - 10
        prix2 = quantite2 * 0.09
        prixTTC = prix1 + prix2
    else :
        prix1 = 0.1*nbPhoto
        quantite = nbPhoto
        prixTTC = prix1
    print ("**************************************************")
    print ("Facture pour ", nbPhoto, "impressions :")
    print ("                            Nb         Montant")
    print ("impressions à 0.10 euro : ", f"{quantite:>3.0f}", "       ", f"{prix1:>2.2f}", "euro")
    print ("impressions à 0.09 euro : ", f"{quantite2:>3.0f}", "       ", f"{prix2:>2.2f}", "euro")
    print ("impressions à 0.08 euro : ", f"{quantite3:>3.0f}", "       ", f"{prix3:>2.2f}", "euro")
    print ("**************************************************")
    print ("Total : ", prixTTC)
    return 
    
def lePlusGrand(a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
    
def multiSansMulti(a,b):
    c = 0
    if b > 0:
        for i in range(0, b, 1):
            c = c + a
    elif b < 0:
        for i in range(0, b, -1):
            c = c - a
    else:
        return "nombre nul"
    if c < 0:
        return "nombre négatif"
    else:
        return "nombre positif"
    

def count():
    for i in range(0, 101):
        print (i)
    return
    
def count2():
    for i in range(4, 86, 3):
        print (i)
    return
    
def count3():
    for i in range(1000, 499, -10):
        print (i)
    return
    
def count4():
    for i in range(1,21):
        print (i**2)
    return
    
def count5():
    for i in range(1,101):
        if (i%2 == 0 or i%3 ==0):
            print (i)
    return
    
def count6():
    for i in range(5,15):
        print(i)
    return

def count7():
    for i in range(0,41,2):
        print(i)
    return

def count8():
    for i in range(10,2,-1):
        print(i)
    return

def count9():
    for i in range(40,-1, -2):
        print(i)
    return
    
def text(n):
    for i in range(0,n):
        print("hello")
    return

def mouton(nb):
    print(1, " mouton ...")
    for i in range(2, nb+1):
        print(i, " moutons ...")
    return

    
def exo7(n):
    u = 3
    for k in range(1, n+1):
        u = u*4
    print (u)
    return

def exo3a():
    var = 0
    for i in range(1,11):
        var = var+i
        print(i)
    return var
    
def exo3b():
    var = 0
    for i in range(1,21,2):
        var = var+i
        print(i)
    return var
    
def exo3c():
    var = 1
    for i in range(1,5):
        var = var*i
        print (i)
    return var

def exo3d():
    var = 0
    for i in range(1,11):
        var = var + (1/i)
        print(i)    
    return var
    
    
def etoiles(nb):
    for i in range(1, nb+1):
        print('*'*i)
    return
    
def multi7v1():
    multi = 0
    for i in range(1,500):
        if i%7 == 0:
            multi = multi+1
    return multi
    
import math
def tripletPhytagoriciens():
    for a in range(1,101):
        for b in range(a,101):
            somme = (a**2+b**2)**0.5
            if (somme == int(somme) and somme <= 100):
                print(a, "\t", b, "\t", int(somme))
            
    return "fini"
    
'''
''' 
def puissanceDe2(nb):
    k = 1
    if nb == 0:
        return 0
    while k <= nb and k*2 <= nb:
        k = k*2
    return k
    
    
def verif10a20():
    nb = 0
    while nb < 10 or nb > 20 :
        nb = int(input('erreur veuillez un nombre entre 10 et 20 : '))
    return nb



def divEucli(a, b):
    q = 0
    while a > b:
        a = a-b
        q = q+1
    return q, a

def boucle1():
    i = 1
    while i < 6:
        i = i+1
    return

def boucle2():
    i = 0
    while i < 101 :
        i = i + 10
    return


from random import *
def game():
    random = randrange(100)+1
    test = int(input("essayer de choisir un nombre : "))
    while random != test:
        if test < random:
            test = int(input("essayer un nombre plus grand : "))
        else :
            test = int(input("essayer un nombre plus petit :"))
        
    return("gagner")

def ordiGame(nb):
    petit = 0
    grand = 100+1
    random = randrange(petit, grand, 1)
    while random != nb:
        print(random)
        result = input(" plus grand ou plus petit ? ")
        if result == "plus grand":
            petit = random+1
            random = randrange(petit, grand, 1)
        else :
            grand = random
            random = randrange(petit, grand, 1)
    return("j'ai gagné")
        
def don():
    cagnot = 0
    nombreDon = 0
    while (cagnot <= 200 and nombreDon < 5):
        donation = int(input("Un petit don ? "))
        cagnot = cagnot + donation
        print("La cagnot est de ", cagnot, "€")
        nombreDon = nombreDon+1
    return(nombreDon)

def spectacle():
    place = 100
    groupe = 0
    nbTotalPersonne = 0
    while place > nbTotalPersonne:
        nbPersonne = int(input("nombre De personne ? "))
        if nbPersonne > 3:
            groupe = groupe + 1
            nbTotalPersonne = nbPersonne + nbTotalPersonne
        else :
            print("votre groupe est trop petit")
    print("Il y a ", nbTotalPersonne, " personnes pour ", groupe, " groupe(s)")
    return

def nombrejusqua(nb):
    somme = 0
    diviseur = 1
    while somme < nb:
        somme = somme + 1/diviseur
        diviseur = diviseur+1
    return diviseur


def toutesLesPuissansesDe2(nb):
    puissance = 1
    binaire = 0
    while puissance > 0:
        puissance = puissanceDe2(nb)
        print(puissance, ", ")
        nb = nb - puissance
        if puissance >= 1:
            expo = 0
            while puissance > 1:
                puissance = puissance/2
                expo = expo + 1
            binaire = binaire + 10**expo
    return binaire

def binaireToNumber(binaire):
    resultat = 0
    puissance = 0
    while binaire > 0:
        if binaire % 10 == 1:
            resultat = resultat + 2**puissance
        elif binaire % 10 != 0:
            return("erreur de frappe")
        puissance = puissance + 1
        binaire = binaire // 10
    return resultat

def perim_rect(a, b):
    return ((a+b)*2)

def aire_rect(a, b):
    return (a*b)

def perim_carre(a):
    return perim_rect(a, a)

def aire_carre(a):
    return aire(a, a)


def OuiOuNon():
    reponse = input("saisir Oui ou Non : ")
    while reponse != "Oui" and reponse != "Non":
        reponse = input("saisir Oui ou Non : ")
    if reponse == "Oui":
        return True
    else :
        return False


def between0at10(nombre):
    return (nombre<=10 and nombre>=0)


def mystere(mini, maxi):
    return randint(mini, maxi)

def exoMulti(mini, maxi):
    multi1 = mystere(mini, maxi)
    multi2 = mystere(mini, maxi)
    print(multi1, " x ", multi2, " = ? ")
    reponse = int(input())
    return (reponse == (multi1 * multi2))
        
def exoAddi(mini, maxi):
    nombre1 = mystere(mini, maxi)
    nombre2 = mystere(mini, maxi)
    print(nombre1, " + ", nombre2, " = ? ")
    reponse = int(input())
    return (reponse == (nombre1 + nombre2))

def exoSoutra(mini, maxi):
    nombre1 = mystere(mini, maxi)
    nombre2 = mystere(mini, maxi)
    print(nombre1+nombre2, " - ", nombre1, " = ? ")
    reponse = int(input())
    return (reponse == nombre2)    
    
def exoDivi(mini, maxi):
    nombre1 = mystere(mini, maxi)
    nombre2 = mystere(mini, maxi)
    print(nombre1 * nombre2, " / ", nombre2, " = ?")
    reponse = int(input())
    return (reponse == nombre1)

def multiMulti(mini, maxi):
    resultat = 0
    for i in range(0, 5):
        if (exoMulti(mini, maxi)):
            resultat = resultat + 1
    return resultat


def exoOpertation(mini, maxi):
    resultat = 0
    for i in range(0,5):
        oper = randint(1,4)
        if oper == 1:
            if (exoMulti(mini, maxi)):
                resultat = resultat + 1
            else :
                maxi = maxi - 1
        elif oper == 2:
            if (exoAddi(mini, maxi)):
                resultat = resultat + 1
            else :
                maxi = maxi - 1
        elif oper == 3:
            if (exoSoutra(mini, maxi)):
                resultat = resultat + 1
            else :
                maxi = maxi - 1
        else :
            if (exoDivi(mini, maxi)):
                resultat = resultat + 1
            else :
                maxi = maxi - 1
    print("vous avez obtenue", resultat, "/ 5")
    return
'''

glob = "oui"
def test(nb):
    glob = "slt"
    loc = nb
    print(glob)
    for k in range(1,100):
        if k<nb :
            print(k)
        else :
            return k

def apres(nb):
    nomb = nb
    if nomb % 2 == 0:
        return nomb//2
    return nomb*3+1

def suite_nombre(nombr):
    nombre = nombr
    tempsVol = 0
    altMax = 0
    while (nombre != 1):
        nombre = apres(nombre)
        tempsVol = tempsVol + 1
        if (altMax < nombre):
            altMax = nombre
    return (tempsVol, altMax)

def tempsAlti(mini, maxi):
    tempsVolValue = 0
    tempsVol = 0
    altMaxValue = 0
    altMax = 0
    tempsVol12 = 0
    tempsVolAvant = 0
    podiumTempsVol = [0, 0, 0]
    for i in range(mini, maxi+1):
        values = suite_nombre(i)
        
        if (values[0] == 12):
            tempsVol12 = tempsVol12 + 1
            
        if (tempsVolValue < values[0]):
            tempsVolValue = values[0]
            tempsVol = i
            
        if (altMaxValue < values[1]):
            altMaxValue = values[1]
            altMax = i
            
        if (tempsVolAvant == values[0]):
            print(i-1, i," ont le meme temps de vol avec ", tempsVolAvant)
        tempsVolAvant = values[0]
    
        if (podiumTempsVol[0] <= values[0]):
            podiumTempsVol[0:3] = [values[0], podiumTempsVol[1:2]]
        elif (podiumTempsVol[1] <= values[0]):
            podiumTempsVol[1:3] = [values[0], podiumTempsVol[2]]
        elif (podiumTempsVol[2] <= values[0]):
            podiumTempsVol[2] = [values[0]]
    print("il y a ", tempsVol12," qui ont un temps de vol = 12")
    print("le plus grand temps de vol est obtenu avec ", tempsVol, " pour ", tempsVolValue, " étapes")
    print("la plus grande altitude est obtenu avec ", altMax, " avec ", altMaxValue)
    print("le podium est ", podiumTempsVol[:])
    return






def nombreE(chaine):
    nbE = 0
    for i in range(0,len(chaine)):
        if chaine[i] == "e":
            nbE += 1
    return nbE

def ou1erEspace(chaine):
    position = -1
    for i in range(0,len(chaine)):
        if chaine[i] == " ":
            position = i
            return position
    return position
    
def inverse(texte):
    lInverse = ""
    for i in range(0, len(texte)):
        lInverse = lInverse + texte[-i-1]
    return lInverse
    
def palindromme(texte):
    return inverse(texte) == texte


def triangleEtoile(n, symbole):
    ligne = ""
    nombre = " " * (n +1)
    for i in range(n):
        ligne = nombre + symbole * (1 + 2*i)
        nombre = " " * (n - i)
        print (ligne)
    return

def supprime(chaine, chara):
    result = ""
    for i in range(len(chaine)):
        if chaine[i] != chara :
            result = result + chaine[i]
    return result

def modif(chaine, oldChara, newChara):
    result = ""
    for i in range(len(chaine)):
        if chaine[i] != oldChara :
            result = result + chaine[i]
        else :
            result = result + newChara
    return result

def compte(chaine, chara):
    nombre = 0
    for i in range(len(chaine)):
        if chaine[i] == chara:
            nombre += 1
    return nombre

def echange(chaine, chara1, chara2):
    result = ""
    for i in range(len(chaine)):
        if chaine[i] == chara1:
            result = result + chara2
        elif chaine[i] == chara2:
            result = result + chara1
        else :
            result = result + chaine[i]
    return result

def parenthese(expression):
    x = 0
    for l in expression:
        if l == "(":
            x = x+1
        elif l == ")":
            x = x-1
        if x < 0:
            return False
    return x == 0

def nombreCharaOk(chaine):
    return len(chaine) == 13


def estInt(chaine):
    return(chaine[0] == "0" or chaine[0] == "1" or chaine[0] == "2" or chaine[0] == "3" or chaine[0] == "4" or chaine[0] == "5" or chaine[0] == "6" or chaine[0] == "7" or chaine[0] == "8" or chaine[0] == "9")
        

def tousDesChiffres(chaine):
    for chara in chaine:
         if (estInt(chara) != True):
             return False
    return True

def hommeOrFemme(chara):
    return(chara[0] == "1" or chara[0] == "2")

def anneeGood(chaine):
    return(tousDesChiffres(chaine) and int(chaine[3:5]) <= 12 and int(chaine[3:5]) >= 0) 


def nbMot(phrase):
    """
    fonction qui compte le nombre de mot
    
    """
    if (len(phrase) == 0 or phrase[0] in {" ", ", ", ". ", "-"}):
        mot = 0
    else :
        mot = 1
    for i in range(len(phrase)):
        if ((phrase[i] in {" ", ", ", ". ", "-"}) and (i+1 < len(phrase)) and phrase[i+1] != {" ", ", ", ". ", "-"}):
            mot += 1
    return mot
            
            
            
lettres = ['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']  
  
def positionLettre(lettre):
    """
    donne la position de la lettre dans l'alphabet
    """
    for i in range(len(lettres)):
        if lettre == lettres[i]:
            return i+1
    return -1


def lettreFreq(phrase):
    """
    content le nombre de lettre et renvoie la plus frequente
    """
    #compte les lettres
    nb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for l in phrase:
        posiLettre = positionLettre(l) 
        nb[posiLettre-1] = nb[posiLettre-1] + 1
       
    #donne la lettre la plus utilisé
    maxi = 0
    for i in range(0, len(nb)):
        if nb[i] > maxi:
            lettre = lettres[i]
            maxi = nb[i]
        
    return max(nb), lettre


def verifRom(nbRom):
    for i in nbRom:
        if i not in {"I", "V", "X", "L", "C", "D", "M"}:
            return False
    return True

'''
def nbRomToDec(nbRom):
    if not verifRom(nbRom):
        return False
    result = 0
    for i in nbRom:
        if i == "I":
            result += 1
        if i == "X":
            result += 10
        if i == "C":
            result += 100
        if i == "M":
            result += 1000
    return result

def nbDecToRom(nbDec):
    result = ""
    if nbDec // 1000 > 0:
        result = result + "M"*(nbDec // 1000)
        nbDec = nbDec%1000
    if nbDec // 100 > 0:
        result = result + "C"*(nbDec // 100)
        nbDec = nbDec%100
    if nbDec // 10 > 0:
        result = result + "X"*(nbDec // 10)
        nbDec = nbDec%10
    result = result + "I"*nbDec
    return result
'''

def nbRomToDec(nbRom):
    if not verifRom(nbRom):
        return False
    result = 0
    teste = False
    for i in range(len(nbRom)):
        if teste:
            teste = False
        elif nbRom[i] == "M" :
            if ((i+1 < len(nbRom)) and nbRom[i+1] == "C"):
                result += 900
                teste = True
            else :
                result += 1000
        elif nbRom[i] == "D" :
            if i+1 < len(nbRom) and nbRom[i+1] == "C":
                result += 400
                i += 1
            else :
                result += 500
        elif nbRom[i] == "C" :
            if i+1 < len(nbRom) and nbRom[i+1] == "X":
                result += 90
                i += 1
            else :
                result += 100
        elif nbRom[i] == "L" :
            if i+1 < len(nbRom) and nbRom[i+1] == "X":
                result += 40
                i += 1
            else :
                result += 50
        elif nbRom[i] == "X" :
            if i+1 < len(nbRom) and nbRom[i+1] == "I":
                result += 9
                i += 1
            else :
                result += 10
        elif nbRom[i] == "V" :
            if i+1 < len(nbRom) and nbRom[i+1] == "I":
                result += 4
                i += 1
            else :
                result += 5
        elif nbRom[i] == "I":
            result += 1
    return result
    
    
tab1 = [4,2,6,2]
tab2 = [3,1,8]

def tabExo1(tab):
    a = tab[0]
    k = 0
    while k < len(tab):
        if a < tab[k]:
            a = tab[k]
        k = k + 1
    return a



def nombreJusquaN(nb):
    tab = []
    for i in range(1, (nb+1)):
        tab.append(i)
    return tab

def plusPetit(tab):
    test = tab[0]
    for i in range(1, len(tab)):
        if test > tab[i]:
            test = tab[i]
    return test

def plusGrand(tab):
    test = tab[0]
    for i in range(1, len(tab)):
        if test < tab[i]:
            test = tab[i]
    return test

def multiElemTab(tab):
    for i in range(len(tab)):
        tab[i] = tab[i]*2
    return tab

def sommeTab(tab):
    somme = 0
    for i in range(len(tab)):
        somme += tab[i]
    return somme

def moyenneTab(tab):
    return (sommeTab(tab)/len(tab))


def ouEstTab(tab, nb):
    for i in range(len(tab)):
        if tab[i] == nb:
            return i
    return -1

def supprInTab(tab, nb):
    result = []
    for i in range(len(tab)):
        if tab[i] != nb:
            result.append(tab[i])
    return result

def supprImpaire(tab):
    result = []
    for i in range(len(tab)):
        if tab[i]%2==0:
            result.append(tab[i])
    return result

def saisieTab(taille):
    result = []
    for i in range(taille):
        phrase = "Saisir l'élément " + str(i) + " : "
        result.append(input(phrase))
    return result

from random import * 
def tabAlea(taille):
    result = []
    for i in range(taille):
        result.append(randint(0, 10))
    return result

def motApresMot(phrase):
    result = []
    mot = ""
    for l in phrase:
        if l != " ":
            mot += l
        else :
            result.append(mot)
            mot = ""
    if mot != "":
        result.append(mot)
    return result

def supPlusGrand(tab):
    lePlusGrand = plusGrand(tab)
    return supprInTab(tab, lePlusGrand)


def supprDoublon(tab):
    result = []
    for i in range(len(tab)):
        add = True
        for k in range(len(result)):
            if result[k] == tab[i]:
                add = False
        if add:
            result.append(tab[i])
    return result







































