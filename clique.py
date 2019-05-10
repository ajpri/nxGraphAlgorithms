import networkx as nx
from itertools import *
from functions.global_properties import V
from functions.local_properties import neighbors
G = nx.read_edgelist('graph_library/pan.txt')


def is_clique(G,S): #set of vertices where every pair in the set forms an edge
    """Returns True if every two distinct vertices are adjacent

    Parameters
    ----------

    G:
        A Graph containg vertices and edges contained in Graph G
    
    S: 
        A constant 
    
    Returns 
    -------

    Bool
        Returns True if every two distinct vertices are adjacent 
     
    """    
    for v in S:
        if list(set(S)&set(neighbors(G,v))) != []:  #[] <-- empty list
            return False
    
    return True


def largest_clique_set(G):
    
"""Returns True if every two distinct vertices are adjacent

    Parameters
    ----------

    G:
    A Graph containg vertices and edges contained in Graph G
    
    S:
    
    Returns 
    -------
    x
        The maximum clique of the Graph

    """    
    n = len(V(G))
    for x in range(n,2,-1):    #increasing
        for x in combinations(V(G),x):
            if is_clique(G,x) == True:
                return x

print('Largest Clique:',largest_clique_set(G))
