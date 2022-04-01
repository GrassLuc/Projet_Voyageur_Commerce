import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def creerPlan(n):
    plateau = []
    for i in range(n):
        k = []
        for j in range(n):
            k.append(0)
        plateau.append(k)
    #print(plateau)
    x = []
    y = []
    i = 0
    while i < n:
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        if plateau[-b-1][a] == 0:
            plateau[-b-1][a] = i+1
            i+=1
            x.append(a+1)
            y.append(b+1)
        #print (i)
        #print(plateau)
    #plt.plot(x,y,"o")

    print(*plateau, sep="\n")
    return plateau,x,y

def villeTousChemin(n):
    plateau,x,y=creerPlan(n)
    c = calculerCout(x,y)
    G = nx.Graph()
    k = 0
    #G.add_node(1)
    G.add_nodes_from([i for i in range(1,n+1)])
    for i in range(1,n):
        for j in range(i+1,n+1):
            nx.add_path(G, [i, j],weight=c[k])
            k+=1
    #print(k)
    plt.subplot(122)
    nx.draw_shell(G, nlist=[range(1, n+1), range(n//2)], with_labels=True, font_weight='bold')
    #nx.draw(G, with_labels=True, font_weight='bold')
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('les positions des villes')
    plt.xlabel('X')
    plt.ylabel('Y')
    ax1.scatter(x,y,s=10,c='r',marker='o')
    plt.legend('villes')
    plt.show()
    return G

def calculerCout(x,y):
    c=[]
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            c.append(np.sqrt((y[j]-y[i])**2+(x[j]-x[i])**2))
    return c


G=villeTousChemin(10)
