import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import pdb
import networkx as nx  # pour la figure topoligique
import time  # Pour calculer le temps
import itertools  # pour les permutations
import dessiner
from tqdm import tqdm

'''
G = dessiner.Graph(10) pour creer une figure n*n
G.calculerCout() pour calculer les distances entre les villes
G.graphNx() creer une topologique avec poids de path
G.afficherEuclidien()
G.afficherTopologique()
dict(nx.all_pairs_dijkstra(G)) G cote entre chaque ville 
'''


#bruteforce
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

#tempsBruteforce(9)


def relationNombreEtTemps(n):
    x = []
    y = []
    k = 0
    with tqdm(total=n-1) as bar:
        for i in range(2, n+1):
            x.append(i)
            bar.update(1)
            for _ in range(5):
                k += tempsBruteforce(i)
            y.append(k/5)
    plt.figure()
    plt.plot(x, y, markersize=2, label='temps')
    plt.xlabel('nombre de point')
    plt.ylabel('temps')
    plt.title('Fonction de temps en nombre de point')
    plt.legend()

    plt.figure()
    plt.plot(x, y, markersize=2, label='temps')
    plt.yscale("log")
    plt.xlabel('nombre de point')
    plt.ylabel('temps')
    plt.title('Fonction de temps en nombre de point')
    plt.legend()
    plt.show()

'''relationNombreEtTemps(12)'''

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
    with tqdm(total=n-1) as bar:
        for i in range(2, n+1):
            x.append(i)
            bar.update(1)
            for _ in range(5):
                k += tempsApproche(i)
        #print(i,k/5)
            y.append(k/5)
    plt.figure()
    plt.plot(x, y, markersize=2, label='temps')
    plt.xlabel('nombre de point')
    plt.ylabel('temps')
    plt.title('Fonction de temps en nombre de point')
    plt.legend()

    plt.figure()
    plt.plot(x, y, markersize=2, label='temps')
    plt.yscale("log")
    plt.xlabel('nombre de point')
    plt.ylabel('temps')
    plt.title('Fonction de temps en nombre de point')
    plt.legend()
    plt.show()

'''relationNombreEtTempsApproche(1000)'''

#1000 fois pour M sur bruteforce et approchee n=9
'''dB = []
dA = []
with tqdm(total=1000) as bar:
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
print('le temps moyenne de la longueur par brute force:',
      np.mean(dB), 'ecart-type', np.std(dB),'max',np.max(dB),'min',np.min(dB))
print('le temps moyenne de la longueur par approchee:',
      np.mean(dA), 'ecart-type', np.std(dA),'max',np.max(dA),'min',np.min(dA))
plt.figure()
plt.boxplot([dA, dB], vert=False, whis=[0, 100], showmeans=True)
plt.show()'''

#1000 fois pour M sur approchee n=200
'''dA = []
with tqdm(total=1000) as bar:
    for _ in range(1000):
        G = dessiner.Graph(200)
        G.calculerCout()
        G.graphNx()
        G.minLongueurApprochee()
        dA.append(G.longueurSomme(G.path))
        bar.update(1)
print('ici on cherche le resultat sur approchee en cas n=200 et s=n**2')
print('le temps moyenne de la longueur par approchee:',
      np.mean(dA), 'ecart-type', np.std(dA),'max',np.max(dA),'min',np.min(dA))
plt.figure()
plt.boxplot(dA, vert=False, whis=[0, 100], showmeans=True)
plt.show()'''

#comparaison entre les resultats de brute force et approchee
'''G = dessiner.Graph(10)
G.calculerCout()
G.graphNx()
G.allPath()
G.minLongueurBruteForce()
G.minLongueurApprochee()
G.afficherResultat(G.t)
G.afficherResultat(G.path)'''

#10 fois pour vérifier sur approchee n=200
'''dA = []
with tqdm(total=10) as bar:
    for _ in range(10):
        G = dessiner.Graph(200)
        G.calculerCout()
        G.graphNx()
        G.minLongueurApprochee()
        dA.append(G.longueurSomme(G.path))
        bar.update(1)
print('ici on vérifie le résultat sur approchee en cas n=200 et s=n**2')
x = np.arange(1,len(dA)+1)
plt.figure()
plt.title('L\'efficacité de la méthode approchee en 200 villes')
plt.xlabel('fois')
plt.ylabel('longueur')
plt.scatter(x,dA,s=10,c='r',marker='o',label='longueur')
plt.plot(x,dA,'-')
plt.legend()
plt.show()'''

#10 fois pour vérifier sur BF et approchee n=9
dB = []
dA = []
with tqdm(total=10) as bar:
    for _ in range(10):
        G = dessiner.Graph(9)
        G.calculerCout()
        G.graphNx()
        G.allPath()
        G.minLongueurBruteForce()
        dB.append(G.d)
        G.minLongueurApprochee()
        dA.append(G.longueurSomme(G.path))
        bar.update(1)
print('ici on vérifie le résultat sur bruteforce et approchee en cas n=9 et s=n**2')
x = np.arange(1,len(dA)+1)
plt.figure()
plt.title('L\'efficacité de la méthode BF et approchee en 9 villes')
plt.xlabel('fois')
plt.ylabel('longueur')
plt.scatter(x,dA,s=10,c='r',marker='o',label='longueur MA')
plt.scatter(x,dB,s=10,c='g',marker='o',label='longueur MBF')
plt.plot(x,dA,'-')
plt.plot(x,dB,'-')
plt.legend()
plt.show()
