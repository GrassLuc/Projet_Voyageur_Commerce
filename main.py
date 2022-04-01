import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import pdb
import networkx as nx #pour
import time #Pour calculer le temps
import itertools #pour les permutations
import dessiner

# Pour creer n villes dans une figure n*n





#bruteforce
def distance_p1p2(p1,p2):
    d= sqrt((p2[0]-p1[0])**2 - (p2[1]-p1[2])**2
    return d

def gen_positions_villes(n,L): #n nombre de ville et L taille du "pays" [0,L]*[0,L]
    T=[]
    for i in range(n):
        T.append((random.randint(0,L),random.randint(0,L))
    return T


def bruteforce(T):
    print(T)
    for i in range(n):


    print('Hello World')




start = time.clock()

# la fonction()

end = time.clock()


print(str(end - start))
