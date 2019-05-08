# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:34:24 2019

@author: Shadow
"""

from functions.global_properties import V
from functions.global_properties import E


def edge_cost (G,e):
    """Returns the cost of a given edge"""
    return G[e[0]][e[1]]['weight']


def incident_edges(G,T):
    """Returns a list of edges adjacent to the starting vertex"""
    incident_e = []
    for e in E(G):
        if e[0] in V(T) or e[1] in V(T):
            if e[0] not in V(T) or e[1] not in V(T):
                incident_e.append(e)
    return incident_e

def minimum_incident_edge(G,T):
    """Returns the edge with the lowest cost"""
    incident_e = incident_edges(G, T)
    min_e = incident_e[0]
    for e in incident_e:
        if edge_cost(G, e) < edge_cost(G,e):
            min_e = e
    return min_e
    

# Still need Prims