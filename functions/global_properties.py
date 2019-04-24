import networkx as nx
from functions.local_properties import neighbors

def V(G):
    return nx.nodes(G)

def E(G):
    return nx.edges(G)

def n(G):
    return len(V(G))

def m(G):
    return len(E(G))

def radius(G):
    return min([eccentricity(G,v) for v in V(G)])

def diameter(G):
    return max([eccentricity(G,v) for v in V(G)])

def maxmimum_degree(G):
    return degree_sequence(G)[0]

def minimum_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree_sequence(G)) / n(G)

def degree_sequence(G):
    D = [degree(G,v) for v in V(G)]
    D.sort(reverse = True)
    return D

def eccentricity(G,v):
    return len(distance_array (G,v)) - 1

def degree(G, v):
    return len(neighbors(G,v))

def distance_array(G, v):
    N = [[v]]
    Obs = [v]
    i = 1
    while set(Obs) != set(V(G)):
        temp_neighbors = []
        for x in N[-1]:
            for y in neighbors(G,x):
                if y not in Obs:
                    temp_neighbors.append(y)
                    Obs.append(y)
        N.append(temp_neighbors)
        print (f'Iteration {i} = {N}')
        i += 1
    