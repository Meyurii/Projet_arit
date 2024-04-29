import random
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
        return (reversed_tableau)
    


grille_tournante = Grille_tournante("proutcacaboudin",6)
grille_tournante.creation_cle()
grille_tournante.creuser_tableau()

def print_tab(tab) : 
    for x in tab :
        print(x)

print_tab(grille_tournante.cle)
print("")
print_tab(grille_tournante.tourner_90_degres_horraire())