import networkx as nx
from functions.local_properties import neighbors

#Returns list of vertices
def V(G):
    return nx.nodes(G) 

#Returns list of edges
def E(G):
    return nx.edges(G)  

#Returns number of Verticies
def n(G):
    return len(V(G)) 

#number of edges (size)
def m(G):
    return len(E(G))    


#############################################################################

#returns the length of neighbors
def degree(G,v):
    return len(neighbors(G,v))

#print(neighbors(G, '5'))

#returns the degree_sequence
def degree_sequence(G):
    D = [degree(G,v) for v in V(G)]
    D.sort(reverse = True)
    return D

#returns the maximum degree
def maxmimum_degree(G):
    return degree_sequence(G)[0]

#returns the minimum degree
def minimum_degree(G):
    return degree_sequence(G)[-1]

#returns the average of the degree
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

