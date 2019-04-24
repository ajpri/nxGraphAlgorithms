import networkx as nx

from itertools import repeat

from functions.global_properties import *

from functions.local_properties import neighbors

G = nx.read_edgelist('graph_library/pan.txt')


def maximal_matching(G,M):
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
    return len(maximal_matching(G,M))

#print('Matching Number:', matching_number(G))
