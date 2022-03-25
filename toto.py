print('Hellow World')
import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import pdb

class Morpion:

    'un joueur de Morpion'
    humain = 1
    ordinateur = -1
    etapeCount = 0
    def __init__(self,firstPlayer):
        'definie un plareau et first player'
        self.plateau = [[0,0,0],[0,0,0],[0,0,0]]
        self.firstPlayer = firstPlayer
        print(self.firstPlayer)

    def afficherplateau(self):
        'pour afficher le plateau'
        self.AfPt = []
## Dupliquer le list sinon ça changera le plateau.
        self.AfPt.extend(copy.deepcopy(self.plateau))
        #print(self.plateau)
        #print(self.AfPt)
        for i in range(3):
            for j in range(3):
                if self.AfPt[i][j] == 0:
                    self.AfPt[i][j] = " "
                elif self.AfPt[i][j] == 1:
                    self.AfPt[i][j] = 'X'
                elif self.AfPt[i][j] == -1:
                    self.AfPt[i][j] = 'O'
##Affichier le list avec un entre apès chaque element.
        print(*self.AfPt,sep="\n")
        return self.plateau

    def joueurHumain(self,x,y):
        'humain player'
        if x >=4 or y >=4:
## stupid humain gamer makes mistake always.
            print('cette case n\'est pas dans le plateau.')
            return False
        elif self.plateau[x-1][y-1] == 0:
            self.plateau[x-1][y-1] = int(1)
            return self.plateau
        else:
## stupid humain gamer makes mistake always.
            print('cette case n\'est pas vide.')
            return False

    def trouverCaseVide(self):
        'chercher de case vide'
        self.caseVide = []
        for i in range(3):
            for j in range(3):
                if self.plateau[i][j] == 0:
                    self.caseVide.append([i,j])
        return self.caseVide

    def joueuraleatoire(self):
        'ordinateur player'
## Ordinateur ne met que dans la case vide.
        Morpion.trouverCaseVide(self)
        self.p = random.randint(0,len(self.caseVide)-1) #trouver une position aleatoire
        self.plateau[self.caseVide[self.p][0]][self.caseVide[self.p][1]]=-1
        return self.plateau

    def checkgagnant(self):
        'verifier qui est gagne'
## Si il y a un gagnant renvoie False,sinon True
        Morpion.trouverCaseVide(self)
        self.somme_ligne = 0
        self.somme_colonne = 0
        self.somme_oblique = 0
        self.somme_antiOblique = 0
        self.gagne = 0
## Quand il y a case vide
        if self.caseVide:
            for i in range(3):
                for j in range(3):
                    self.somme_ligne += self.plateau[i][j]
                    self.somme_colonne += self.plateau[j][i]
                    if self.somme_ligne == 3 or self.somme_colonne == 3:
                        print('humain')
                        self.gagne = 1
                        return False

                    elif self.somme_ligne == -3 or self.somme_colonne == -3:
                        print('ordinateur')
                        self.gagne = -1
                        return False
## faire le variable verifier est 0
                self.somme_ligne =0
                self.somme_colonne =0
                self.somme_oblique += self.plateau[i][i]
                self.somme_antiOblique += self.plateau[i][-i-1]
                if self.somme_oblique == 3 or self.somme_antiOblique == 3:
                    print('humain')
                    self.gagne = 1
                    return False

                elif self.somme_oblique == -3 or self.somme_antiOblique == -3:
                    print('ordinateur')
                    self.gagne = -1
                    return False

            print('continuez')
            return False
## Q uand il y plus de case vide
        else:
            for i in range(3):
                for j in range(3):
                    self.somme_ligne += self.plateau[i][j]
                    self.somme_colonne += self.plateau[j][i]
                    if self.somme_ligne == 3 or self.somme_colonne == 3:
                        print('humain')
                        self.gagne = 1
                        return False
                    elif self.somme_ligne == -3 or self.somme_colonne == -3:
                        print('ordinateur')
                        self.gagne = -1
                        return False
## faire le variable verifier est 0
                self.somme_ligne =0
                self.somme_colonne =0
                self.somme_oblique += self.plateau[i][i]
                self.somme_antiOblique += self.plateau[i][-i-1]
                if self.somme_oblique == 3 or self.somme_antiOblique == 3:
                    print('humain')
                    self.gagne = 1
                    return False
                elif self.somme_oblique == -3 or self.somme_antiOblique == -3:
                    print('ordinateur')
                    self.gagne = -1
                    return False
            print('None')
            return True

    def checkNull(self):
        if Morpion.checkgagnant == True:
            return True
        else :
            return False

    def gameover(self):
        Morpion.checkgagnant(self)
        if Morpion.checkNull == True:
            return 'la partie est nulle'
        elif self.gagne ==1 :
            return 'un gagnant : humain'
        elif self.gagne ==-1 :
            return 'un gagnant : ordinateur'
        else:
            return False

    def play(self):
        Morpion.afficherplateau(self)
        print(self.firstPlayer)
        if self.firstPlayer == 1:
            Morpion.trouverCaseVide(self)
            while Morpion.gameover(self) == False:
                if Morpion.etapeCount%2:#ici soit il y a rest ,est True. Sinon, est False
                    Morpion.joueuraleatoire(self)
                    Morpion.afficherplateau(self)
                    Morpion.etapeCount+=1
                else:
                    print('your turn, humain')
                    self.l,self.c=(input('ligne et colonne, separe par espace').split())
                    self.l=int(self.l)
                    self.c=int(self.c)
                    self.ph = list()
                    self.ph.append([self.l,self.c])
                    if Morpion.joueurHumain(self,self.ph[0][0],self.ph[0][1]):
                        Morpion.etapeCount+=1
                        Morpion.afficherplateau(self)
            return Morpion.gameover(self)

        elif self.firstPlayer == -1:
            while Morpion.gameover(self) == False:
                if Morpion.etapeCount%2:
                    print('your turn, humain')
                    self.l,self.c=(input('ligne et colonne, separe par espace').split())
                    self.l=int(self.l)
                    self.c=int(self.c)
                    self.ph = list()
                    self.ph.append([self.l,self.c])
                    if Morpion.joueurHumain(self,self.ph[0][0],self.ph[0][1]):
                        Morpion.afficherplateau(self)
                        Morpion.etapeCount+=1
                else:
                    Morpion.joueuraleatoire(self)
                    Morpion.afficherplateau(self)
                    Morpion.etapeCount+=1
            return Morpion.gameover(self)


test = Morpion(1)
test.play()
