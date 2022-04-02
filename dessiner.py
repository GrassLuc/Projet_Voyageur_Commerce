import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

class Graph:
    def __init__(self,n):
        self.plateau = []
        self.n = n
        for i in range(self.n):
            k = []
            for j in range(self.n):
                k.append(0)
            self.plateau.append(k)
            #print(plateau)
        self.x = []
        self.y = []
        i = 0
        while i < self.n:
            a = random.randint(0,self.n-1)
            b = random.randint(0,self.n-1)
            if self.plateau[-b-1][a] == 0:
                self.plateau[-b-1][a] = i+1
                i+=1
                self.x.append(a+1)
                self.y.append(b+1)

    def calculerCout(self):
        self.c=[]
        for i in range(len(self.x)):
            for j in range(i+1,len(self.x)):
                self.c.append(np.sqrt((self.y[j]-self.y[i])**2+(self.x[j]-self.x[i])**2))
        return self.c

    def graphNx(self):# creer une figure topologique avec poids de path
        self.G = nx.Graph()
        k = 0
        self.G.add_nodes_from([i for i in range(1,self.n+1)])
        for i in range(1,self.n):
            for j in range(i+1,self.n+1):
                nx.add_path(self.G, [i, j],weight=self.c[k])
                k+=1
        return self.G

    def afficherEuclidien(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.set_title('les positions des villes')
        plt.xlabel('X')
        plt.ylabel('Y')
        ax1.scatter(self.x,self.y,s=self.n*10,c='r',marker='o')
        plt.legend('villes')
        plt.show()

    def afficherTopologique(self):
        plt.subplot(122)
        nx.draw(self.G, with_labels=True, font_weight='bold')
        #nx.draw_shell(self.G, nlist=[range(1, self.n+1), range(self.n//2)], with_labels=True, font_weight='bold')
        plt.show()
