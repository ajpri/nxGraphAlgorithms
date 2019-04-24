import networkx as nx

def neighbors(G,v):
    return list(nx.neighbors(G,v))


def set_neighbors(G, S):
    N = []
    for x in S:
        N.append(x)

def closed_neighbors(G,v):
    N = neighbors(G,v)
    N.append(v)
    return N
