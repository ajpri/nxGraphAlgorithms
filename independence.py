import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors


def is_independent(G,S):
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
    for v in S:
        if list(set(S) & set(neighbors(G, v))) != []:
            return False
        return True
    
 

def maximum_independent_set(G):
       
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
    n = len(V(G))
    for k in range(n-1,1, -1):
        for s in combinations(V(G),k):
            if is_independent(G,list(s)) == True:
                return list(s)
  

def independence_number(G):
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
        return len(maximum_independent_set(G))

