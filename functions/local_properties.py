import networkx as nx

def neighbors(G,v):
    return list(nx.neighbors(G,v))


def set_neighbors(G, S):
    N = []
    for x in S:
        N.append(x)
        