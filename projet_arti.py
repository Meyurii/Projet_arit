import random
import os
class Grille_tournante:
    def __init__(self, phrase, n):
        self.phrase = phrase
        self.n = n
        self.cle = []

    def creation_cle(self):
        for x in range(self.n):
            self.cle.append([])
            for y in range(self.n):
                self.cle[x].append(0)
    
    def creuser_tableau(self):
        if self.n % 2 == 0:
            case_a_couper = (self.n ** 2) / 4
            verif_paire = True
        else:
            case_a_couper = ((self.n ** 2) - 1) / 4
            verif_paire = False
        case_creuser = 0
        while (case_creuser != case_a_couper) :
            for x in range(len(self.cle)):
                for y in range(len(self.cle[x])):
                    if self.cle[x][y] == 0 and random.randint(0, 5) == 0: #random = proba
                        if(verif_paire == True):
                            self.cle[x][y] = 1
                            case_creuser += 1
                            if case_creuser == case_a_couper:
                                return
                        else:
                            index = (n - 1) // 2
                            if(self.cle[index][index] != 0 and self.cle[x][y] == 0 and random.randint(0, 5) == 0):
                                self.cle[x][y] = 1
                                case_creuser += 1
                                if case_creuser == case_a_couper:
                                    return
                            else:
                                self.cle[x][y] = 1
                                case_creuser += 1
                                if case_creuser == case_a_couper:
                                    return

    def tourner_90_degres_horraire(self):
        tableau_prov = [[0] * self.n for _ in range(self.n)]
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                tableau_prov[y][x] = self.cle[x][y]
        
        reversed_tableau = []
        for row in tableau_prov:
            reversed_row = row[::-1]  # Inverser la ligne
            reversed_tableau.append(reversed_row)
        self.cle = reversed_tableau
        return (reversed_tableau)

    def verif_cle(self, a, b, c, d):
        for x in range (len(self.cle)):
            for y in range (len(self.cle)):
                if (a[x][y] and b[x][y] == 1):
                    return False
                if (a[x][y] and c[x][y] == 1):
                    return False
                if (a[x][y] and d[x][y] == 1): #fin de verif de a
                    return False
                if (b[x][y] and c[x][y] == 1):
                    return False
                if (b[x][y] and d[x][y] == 1): #fin verif b
                    return False
                if (c[x][y] and d[x][y] == 1):
                    return False
            return True

    

def print_tab(tab) : 
    for x in tab :
        print(x)

def final():
    grille_tournante = Grille_tournante("proutcacaboudin",6)
    grille_tournante.creation_cle()
    grille_tournante.creuser_tableau()
    etat1 = grille_tournante.cle
    print_tab(grille_tournante.cle)
    print("")
    etat2 = grille_tournante.tourner_90_degres_horraire()
    print_tab(etat2)
    print("")
    etat3 = grille_tournante.tourner_90_degres_horraire() 
    print_tab(etat3)
    print("")
    etat4 = grille_tournante.tourner_90_degres_horraire() 
    print_tab(etat4)
    if(grille_tournante.verif_cle(etat1, etat2, etat3, etat4) == False):
 
        os.system('cls')
        final()
    else: 
        print("yes")

    




final()



