import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import pdb
import networkx as nx #pour la figure topoligique
import time #Pour calculer le temps
import itertools #pour les permutations
import dessiner


'''
G = dessiner.Graph(10) pour creer une figure n*n
G.calculerCout() pour calculer les distances entre les villes
G.graphNx() creer une topologique avec poids de path
G.afficherEuclidien()
G.afficherTopologique()
dict(nx.all_pairs_dijkstra(G)) G 中每一个点到另一个点的开销
'''



#bruteforce
'''G = dessiner.Graph(10)
G.calculerCout()
G.graphNx()

start = time.time()

G.allPath()
G.minLongueur()

end = time.time()

print(str(end - start))'''

#time of bruteforce
def tempsBruteforce(n):
    G = dessiner.Graph(n)
    G.calculerCout()
    G.graphNx()

    start = time.time()

    G.allPath()
    G.minLongueur()

    end = time.time()

    return float(end-start)

#print(tempsBruteforce(9))

def relationNombreEtTemps(n):
    x = []
    y = []
    k = 0
    for i in range(2,n+1):
        x.append(i)
        for _ in range(5):
            k += tempsBruteforce(i)
        y.append(k/5)
    plt.figure()
    plt.plot(x,y,markersize=2,label='temps')
    plt.xlabel('nombre de point')
    plt.ylabel('temps')
    plt.title('Fonction de temps en nombre de point')
    plt.legend()

    plt.figure()
    plt.plot(x,y,markersize=2,label='temps')
    plt.yscale("log")
    plt.xlabel('nombre de point')
    plt.ylabel('temps')
    plt.title('Fonction de temps en nombre de point')
    plt.legend()
    plt.show()

relationNombreEtTemps(11)
