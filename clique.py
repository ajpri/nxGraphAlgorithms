# -*- coding: utf-8 -*-

import networkx as nx
#from functions.global_properties import V

G = nx.read_edgelist('G.txt')
nodes = G.nodes
#print(V(G))




#def is_clique(G, clique_nodes):
   # for x in clique_nodes:
        #for y in clique_nodes:
            #if x!= y:
                #if not(G.has_edge(x,y)):
                    #return False
    #return True
    
    
def is_clique(G, nodes):
    for x in nodes(nodes, 2):
        if x[1] not in G[x[0]]:
            return False
    return True
#print(is_clique(G,nodes))