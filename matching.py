import networkx as nx

from itertools import repeat

from functions.global_properties import *

from functions.local_properties import neighbors

G = nx.read_edgelist('graph_library/pan.txt')

def maximal_matching(G,M):
    """ Prints a set for  

    Parameters
    ----------
    G : int
    The graph containing the vertices and edges
    M : set
    M is maximal matching if it is not a subset of any other matching in graph G
    
    Returns
    -------
    set 
    a set of 
    """   
    matching = set([])
    edges = set([])
    for u,v in list(E(G)):
        if (u,v) not in edges and (v,u) not in edges:
            matching.add((u,v))
            edges |= set(E(G)(u))
            edges |= set(E(G)(v))
    return matching


#print('Maximal:', maximal_matching(G,M))


def matching_number(G):
    """ Returns the number of maximal matchings

    Parameters
    -----------
    G: int 
    A list containing the vertices and edges of graph G

    Returns
    -------
    int
        a number of how many maximal matching there are
    """    
    return len(maximal_matching(G,M))

#print('Matching Number:', matching_number(G))
