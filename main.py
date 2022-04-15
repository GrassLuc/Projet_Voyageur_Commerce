import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import pdb
import networkx as nx #pour la figure topoligique
import time #Pour calculer le temps
import itertools #pour les permutations
import dessiner
from tqdm import tqdm

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
    G.minLongueurBruteForce()

    end = time.time()

    return float(end-start)

#print(tempsBruteforce(9))

def relationNombreEtTemps(n):
    x = []
    y = []
    k = 0
    with tqdm(total = n-1) as bar:
        for i in range(2,n+1):
            x.append(i)
            bar.update(1)
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

#time of approchee
def tempsApproche(n):
    G = dessiner.Graph(n)
    G.calculerCout()
    G.graphNx()

    start = time.time()

    G.minLongueurApprochee()

    end = time.time()

    return float(end-start)

#print(tempsBruteforce(9))

def relationNombreEtTempsApproche(n):
    x = []
    y = []
    k = 0
    with tqdm(total = n-1) as bar:
        for i in range(2,n+1):
            x.append(i)
            bar.update(1)
            for _ in range(5):
                k += tempsApproche(i)
        #print(i,k/5)
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

#relationNombreEtTempsApproche(150)

dB = []
dA = []
with tqdm(total = 1000) as bar:
    for _ in range(1000):
        G = dessiner.Graph(9)
        G.calculerCout()
        G.graphNx()
        G.allPath()
        G.minLongueurBruteForce()
        dB.append(G.d)
        G.minLongueurApprochee()
        dA.append(G.longueurSomme(G.path))
        bar.update(1)
print('ici on compare sur bruteforce et approchee en cas n=9 et s=n**2')
print('le temps moyenne de la longueur par brute force:',np.mean(dB),'ecart-type',np.std(dB))
print('le temps moyenne de la longueur par approchee:',np.mean(dA),'ecart-type',np.std(dA))
