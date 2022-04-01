import networkx as nx
import matplotlib.pyplot as plt
import random

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
            x.append(a)
            y.append(b)
        #print (i)
        #print(plateau)
    #plt.plot(x,y,"o")
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')

    ax1.scatter(x,y,s=10,c='r',marker='o')
    plt.legend('villes')
    plt.show()
    print(*plateau, sep="\n")
    return plateau

def villeTousChemin(n,s):
    G = nx.Graph()
    #G.add_node(1)
    G.add_nodes_from([i for i in range(1,n+1)])
    G.add_edges_from([(i,j) for i in range(1,n+1) for j in range(1,n+1)])
    nx.draw_shell(G, nlist=[range(1, n+1), range(s)], with_labels=True, font_weight='bold')
    #nx.draw(G, with_labels=True, font_weight='bold')
    return G


creerPlan(10)
