# -*- coding: utf-8 -*-

import networkx as nx



nodes = G.nodes
 
def is_clique(G, nodes):
    for x in nodes(nodes, 2):
        if x[1] not in G[x[0]]:
            return False
    return True
