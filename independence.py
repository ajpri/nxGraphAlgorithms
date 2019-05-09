import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

"""Returns true if 

Parameters
----------
G : int
    The graph containing the vertices and edges of graph G
S : set
    
    

Returns
-------
Bool
    Returns true if the 
"""
def is_independent(G,S):
    for v in S:
        if list(set(S) & set(neighbors(G, v))) != []:
            return False
        return True
    
    
"""Returns the list of the maximum possible independent set

Parameters
----------
G : int
    The graph containg the vertices and edges of graph G
    
Returns
-------
list
    a list of the maximum possible independent set
"""


def maximum_independent_set(G):
    n = len(V(G))
    for k in range(n-1,1, -1):
        for s in combinations(V(G),k):
            if is_independent(G,list(s)) == True:
                return list(s)
  
"""Returns the list of the maximum possible independent set

Parameters
----------
G : int
    The graph containg the vertices and edges of graph G
    
Returns
-------
int
    Returns a number of the largest independent vertex set

"""
def independence_number(G):
    return len(maximum_independent_set(G))

