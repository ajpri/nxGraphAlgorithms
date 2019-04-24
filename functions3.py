# -*- coding: utf-8 -*-
import networkx as nx
import networkx.algorithms.coloring as ngc
import itertools as it



G = nx.read_edgelist('G.txt')


def V(G):
    return nx.nodes(G)

def E(G):
    return nx.edges(G)

def n(G):
    return len(V(G))

def m(G) :
    return len(E(G))

def neighbors(G,v):
    return list(nx.neighbors(G,v))

def degree(G, v):
    return len(neighbors(G,v))

def degree_sequence(G):
    D = [degree(G,v) for v in V(G)]
    D.sort(reverse = True)
    return D

def max_degree(G):
    return degree_sequence(G)[0]

def min_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree_sequence(G))/n(G)


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
        
    return N

def distance(G, v ,w):
    D = distance_array(G,v)
    for i in range(len(D)):
        if w in D[i]:
            return i
        

def eccentricity(G,v):
    return len(distance_array(G,v))-1

def radius(G):
    return min([eccentricity(G,v) for v in V(G)])

def diameter(G):
    return max([eccentricity(G,v) for v in V(G)])

def graph_center(G):
    return [v for v in V(G) 
            if eccentricity(G,v) == radius(G)]
    
def delete_first_term(L):
    L.pop(0)
    return None

def Havel_hakimi_dervate(L):
    d_1 = L[0]
    L.pop(0)
    for i in range(d_1):
        L[i] -=1
    L.sort(reverse=True)
    return None

nx.draw(G)
#g = ngc.greedy_color(G,'largest_first')    





def getColors(G):
    colors = {}
    for u in V(G):
        neighbour_colors = {colors[v] for v in G[u] if v in colors}
        for color in it.count():
            if color not in neighbour_colors:
                break
        colors[u] = color
    return colors
    
    
print(getColors(G))
edgeList = E(G)

