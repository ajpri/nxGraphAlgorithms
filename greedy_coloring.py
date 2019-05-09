import networkx as nx
from  functions.global_properties import V
from functions.local_properties import neighbors
import itertools as it

"""Returns vertices with their corresponding colors

Parameters
----------
G: int
   A graph containing the vertices and edges contained in graph G
   
Returns
-------
colors 
    Returns vertices with their corresponding colors
"""
def greedy_coloring (G):
    colors = {}
    for u in V(G):
        neighbour_colors = {colors[v] for v in G[u] if v in colors}
        for color in it.count():
            if color not in neighbour_colors:
                break
        colors[u] = color
    return colors
