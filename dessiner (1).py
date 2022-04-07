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

    def longueur(self):
        x0,y0 = self.x[-1], self.y[-1]
        d = 0
        for o in range(len(x)):
            x1,y1 = x[o], y[o]
            d += (x0-x1)**2 + (y0-y1)**2
            x0,y0 = x1,y1
        return d

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
        plt.plot(self.x+[self.x[0]],self.y+[self.y[0]],'-',label='path')
        plt.legend('villes')
        plt.show()

    def afficherTopologique(self):
        plt.subplot(122)
        nx.draw(self.G, with_labels=True, font_weight='bold')
        #nx.draw_shell(self.G, nlist=[range(1, self.n+1), range(self.n//2)], with_labels=True, font_weight='bold')
        plt.show()

    def allPath(self):
        self.allpath=[]
        for i in range(2,self.n+1):
            for path in nx.all_simple_paths(self.G, source=1, target=i):
                if len(path)==self.n:
                    path.append(1)
                    self.allpath.append(path)
        #print(self.allpath)
        return self.allpath

    def longueur(self,path):
        d = 0
        for i in range(len(path)-1):
            d += nx.path_weight(self.G,[path[i],path[i+1]],'weight')
            #print(i,i+1)
        #print(d)
        return d

    def minLongueur(self):
        self.d = self.longueur(self.allpath[0])
        self.t = self.allpath[0]
        for i in range(len(self.allpath)):
            if self.d>self.longueur(self.allpath[i]):
                self.d = self.longueur(self.allpath[i])
                self.t = self.allpath[i]
        print(self.d,self.t)
        return
