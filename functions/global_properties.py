import networkx as nx
from functions.local_properties import neighbors


def V(G):
    return nx.nodes(G)  #vertices

def E(G):
    return nx.edges(G)  #edges

def n(G):
    return len(V(G))    #number of vertices (order)

def m(G):
    return len(E(G))    #number of edges (size)


#############################################################################

def degree(G,v):
    return len(neighbors(G,v))

#print(neighbors(G, '5'))
    
def degree_sequence(G):
    D = [degree(G,v) for v in V(G)]
    D.sort(reverse = True)
    return D

def maxmimum_degree(G):
    return degree_sequence(G)[0]

def minimim_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree_sequence(G)) / n(G)


#############################################################################


def distance_array(G,v):
    N = [[v]]
    Obs = [v]
    i = 1
    while set(Obs) != set(V(G)):
        print(f'Iteration {i} = {N}')
        temp_neighbors = []
        for x in N[-1]:
            for y in neighbors(G,x):
                if y not in Obs:
                    temp_neighbors.append(y)
                    Obs.append(y)
        N.append(temp_neighbors)
        return N

def distance(G,v,w):
    D = distance_array(G,v)
    for i in range(len(D)):
        if w in D[i]:
            return i
        
#############################################################################


def eccentricity(G,v):
    return len(distance_array (G,v)) - 1
def radius(G):
    return min([eccentricity(G,v) for v in V(G)])

def diameter(G):
    return max([eccentricity(G,v) for v in V(G)])

