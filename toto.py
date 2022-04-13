import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import pdb
import networkx as nx #pour
import time #Pour calculer le temps
import itertools #pour les permutations
import dessiner

G = dessiner.Graph(10)
G.calculerCout()
G.graphNx()
G.afficherEuclidien()
G.afficherTopologique()

G = dessiner.Graph(9)
G.calculerCout()
G.graphNx()
G.minLongueurApprochee()
