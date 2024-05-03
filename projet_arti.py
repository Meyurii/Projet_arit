import random
import os
import string

class Grille_tournante:
    def __init__(self, phrase, n): #ici tu initialsé des variables quand tu feras un self.nomdetavariable elle se changera directement
        self.phrase = phrase
        self.n = n
        self.cle = []
        self.cle90 = []
        self.cle180 = []
        self.cle270 = []
        self.crypte = []
        self.decrypte = []
        self.message = []

    def plusieurs_tableaux(self) :
        if self.n % 2 == 0:
            self.message = [self.phrase[i:i+self.n ** 2] for i in range(0, len(self.phrase), self.n ** 2)]
        else :
            self.message = [self.phrase[i:i+self.n ** 2 - 1] for i in range(0, len(self.phrase), self.n ** 2 - 1)]


    def longueur_phrase(self):
        if (self.n**2 > len(self.phrase)):
            Longueur = 0 
        if (self.n**2 == len(self.phrase)):
            Longueur = 1
        if (self.n**2 < len(self.phrase)):
            Longueur = 2
        return Longueur

    def creation_cle(self): #donc ici on crée la clé le n est le nombre de case verticale et horizontale que l'utilsateur souhaite on fait une boucle pour crée n liste puis grace
        for x in range(self.n): # a y on crée des liste de liste comme ca on peut la remplir de 0
            self.cle.append([]) #en résumer on veut juste lui donner une taille ce sera dans la prochaine fonction qu'on lui attribura des 1 (qui sont les cases vide)
            for y in range(self.n):
                self.cle[x].append(0)
    
    def creuser_tableau(self):  #c'est ici qu'on va décider ou et combien de case vont valoir 1 
        if self.n % 2 == 0: 
            case_a_couper = (self.n ** 2) / 4 #ici si c'est pair on applique cette formule (écrite dans l'énoncé) elle nous donne le nombre de case vide qu'on veut
            verif_paire = True #on crée une variable verif pair car dans l'énoncer on veut que si c'est impair le nombre du milieu soit forcement égale a 0
                                #le verfi pair sert alors d'indicateur
        else:
            case_a_couper = ((self.n ** 2) - 1) / 4 #ici si c'est impair on applique cette formule (écrite dans l'énoncé)
            verif_paire = False 
        case_creuser = 0 #on initialise case creuser
        while (case_creuser != case_a_couper) : #ici on comparer le nombre de case vide qu'on a représenté par "case_creuser" tant que ce n'est pas égal au nb de case a creusé représenté
            for x in range(len(self.cle)): #par "case_a_couper". Puis on fait 2 boucles pour rentrer dans la liste de liste
                for y in range(len(self.cle[x])):
                    if self.cle[x][y] == 0 and random.randint(0, 5) == 0: #ici imagine que "random.randint(0, 5) == 0" est une roulette russe c'est a dire qu'on va te donner un nombre entre 
                        if(verif_paire == True):#0 et 5 au hasard si il est = a 0 et qu'a l'index x y est = a 0 alors on rentre dans le if 
                            self.cle[x][y] = 1  #ici nous sommes dans le cas ou c'est pair dans ce cas rien de compliqué on remplace a l index x y le 0 par un 1 sans oublié de rajouté +1
                            case_creuser += 1 # a case creusé
                            if case_creuser == case_a_couper:
                                return #ce if la nous permet de stoper la fonction quand on a atteint l'objectif (pour rappel un return stop une fonction)
                        else: #dans le cas ou c'est impaire
                            milieu = (self.n - 1) // 2 #on cherche le mileu imagine (7-1)//2 on trouve bien 3 qui est le milieu
                            if (x == milieu and y == milieu) :
                                continue
                            self.cle[x][y] = 1 #x et y soit = a 0 et si on tombe sur  grâce au 0 alors on ecrit le 1 et on rajoute une case a "case_creuser"
                            case_creuser += 1
                            if case_creuser == case_a_couper:
                                return #encore une fois pour arreter la fonction


    def tourner_90_degres_horraire(self, tab): #cette fonction sert a faire tourner la grille a 90°
        tableau_prov = [[0] * self.n for _ in range(self.n)] #ici on initialise un tableau en lui donnant une taille.
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):#boucle dans boucle pour accédé aux éléments
                tableau_prov[y][x] = tab[x][y] #ici on prend les ligne qu'on met a la place des colonnes (donc on met des valeurs dans tableau_prov qu'on copie de self.cle)
        
        tableau_a_l_envers = [] #liste vide
        for ligne in tableau_prov: #on passe dans toutes les lignes du tableau provisoir
            ligne_a_lenvers = ligne[::-1]  # Ici on énumaire la ligne a l'envers (en gros)
            tableau_a_l_envers.append(ligne_a_lenvers) #on ajoute les lignes inverser a notre tableau
        #self.cle = tableau_a_l_envers #puis notre clé prend la valeur du tableau pour qu'on puisse la renversé plusieurs fois (sinon ca ne changerai pas car les positions, resterai les mêmes)
        return (tableau_a_l_envers)

    def verif_cle(self, a, b, c, d): #ici on va verifie que dans chaque etat de la clé etat1=a donc avant qu'elle subisse une rotation pusi etat2= b quand elle a subit une 1er rotation etc 
        for x in range (len(self.cle)): #pour c et d car en tout on a besoin de 4 etats on refait deux boucles puis on verifie qu'aucun 1 ne soit 2 fois au même endroits
            for y in range (len(self.cle)):#donc on verfie toute les possibiltés si un seul return retourne False alors la clé est inutilisable
                if (a[x][y] and b[x][y] == 1): #si elle est utilisable alors elle return True
                    return False
                if (a[x][y] and c[x][y] == 1):
                    return False
                if (a[x][y] and d[x][y] == 1): #fin de verif de a
                    return False
                if (b[x][y] and c[x][y] == 1):
                    return False
                if (b[x][y] and d[x][y] == 1): #fin verif b
                    return False
                if (c[x][y] and d[x][y] == 1):#fin de verif c et d
                    return False
        return True


    def crypte_texte(self):
        p=0
        tab_temp1 = [[0] * self.n for _ in range(self.n)]
        tab_temp2 = [[0] * self.n for _ in range(self.n)]
        tab_temp3 = [[0] * self.n for _ in range(self.n)]
        tab_temp4 = [[0] * self.n for _ in range(self.n)]
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if (self.cle[x][y] == 1 and (len(self.phrase) - 1) >= p):
                   tab_temp1[x][y] = self.phrase[p]
                   p += 1
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if (self.cle90[x][y] == 1 and (len(self.phrase) - 1) >= p):
                   tab_temp2[x][y] = self.phrase[p]
                   p += 1
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if (self.cle180[x][y] == 1 and (len(self.phrase) - 1) >= p):
                   tab_temp3[x][y] = self.phrase[p]
                   p += 1
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if (self.cle270[x][y] == 1 and (len(self.phrase) - 1) >= p):
                   tab_temp4[x][y] = self.phrase[p]
                   p += 1

        tab_cryp = [[0] * self.n for _ in range(self.n)]
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if (tab_temp1[x][y] != 0):
                    tab_cryp[x][y] = tab_temp1[x][y]
                if (tab_temp2[x][y] != 0):
                    tab_cryp[x][y] =  tab_temp2[x][y]
                if (tab_temp3[x][y] != 0):
                    tab_cryp[x][y] = tab_temp3[x][y]
                if (tab_temp4[x][y] != 0):
                    tab_cryp[x][y] = tab_temp4[x][y]
                if (tab_cryp[x][y] == 0 or tab_cryp[x][y] == 1) :
                    tab_cryp[x][y] = random.choice("abcdefghijklmnopqrstuvwxyz")
        self.crypte = tab_cryp
        return tab_cryp
    
    def decoder_message(self):
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if self.cle[x][y] == 1 :
                    self.decrypte.append(self.crypte[x][y])
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if self.cle90[x][y] == 1 :
                    self.decrypte.append(self.crypte[x][y])
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if self.cle180[x][y] == 1 :
                    self.decrypte.append(self.crypte[x][y])
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if self.cle270[x][y] == 1 :
                    self.decrypte.append(self.crypte[x][y])
                    
    def save_cle(self):
        chemin_fichier = "cle.txt"
        with open(chemin_fichier, "w") as fichier:
            for x in range (len(self.cle)):
                if x == len(self.cle) - 1 :
                    fichier.write(ligne_str)
                else :
                    ligne_str = "".join(map(str, self.cle[x]))
                    fichier.write(ligne_str + "\n")
    
    def load_cle(self):
        chemin_fichier = "cle.txt"
        with open(chemin_fichier, "r") as fichier:
            contenu = fichier.read()
            separe = contenu.split("\n")
            self.cle = [[0] * len(separe) for _ in range(len(separe))]
            for x in range (len(separe)) :
                for y in range(len(separe)) :
                    self.cle[x][y] = int(separe[x][y])


def print_tab(tab) : #mise en forme en tableau
    for x in tab :
        print(x)

def final(): #ici c'est la fonction final
    while True :
        grille_tournante = Grille_tournante("proutcacaboudinfgbytcsqfgfghsqfgsfsqfgevjhzkjhsxbfsk",6) #ici on inisialise la class
        grille_tournante.creation_cle() #appel des fonction avec le nom de la variable de class.lenomdelafonction
        grille_tournante.creuser_tableau()
        etat1 = grille_tournante.cle #ici on crée les "etats" (il y en a 4 en tout 1 au debut puis 1 autre pour chaque tour) elle prenne les valeurs de la grille
        etat2 = grille_tournante.tourner_90_degres_horraire(etat1)
        etat3 = grille_tournante.tourner_90_degres_horraire(etat2) 
        etat4 = grille_tournante.tourner_90_degres_horraire(etat3)
        grille_tournante.cle = etat1
        grille_tournante.cle90 = etat2
        grille_tournante.cle180 = etat3
        grille_tournante.cle270 = etat4
        if(grille_tournante.verif_cle(etat1, etat2, etat3, etat4) == True): #c'est grâce a ce if qu'on va dire a notre programme quoi faire si la clé n'est pas bonne. Elle regarde si verif avec
            os.system('cls') #comme paramatere etat1, etat2, etat3, etat4 est faux alors elle supprime ce qu'elle a écrit dans la console puis relance la fonction final pour généré une nouvelle 
            grille_tournante.plusieurs_tableaux()
            for x in grille_tournante.message :
                grille_tournante.phrase = x
                print_tab(grille_tournante.crypte_texte())
                print("état 1:")
                print_tab(grille_tournante.cle)
                print("")
                print_tab(etat1)
                print("état 2:")
                print_tab(grille_tournante.cle90)
                print("état 3:")
                print_tab(grille_tournante.cle180)
                print("état 4:")
                print_tab(grille_tournante.cle270)
                print("")
                print("decrypté :")
                grille_tournante.decoder_message()
                print(grille_tournante.decrypte)
                #grille_tournante.save_cle()
                #grille_tournante.load_cle()
                print(grille_tournante.message)
            break



final() #ici on oublie pas d'appeler la foncion
#c'est peut-être pas le plus opti mais ca marche


