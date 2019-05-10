import networkx as nx

def neighbors(G,v):
     """
    Returns the center of the graph
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
    v :     Vertex
            Integer of vertex neighbors            
           
    Returns
    -------
     :   List
     Returns neighbors of a point
    """
    return list(nx.neighbors(G,v))


def set_neighbors(G, S):
    """
    Returns neighbors of a set
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
    S :     Set
            Set of vertexes            
           
    Returns
    -------
     :   List
     Returns set neighbors of a graph
    """
    N = []
    for x in S:
        N.append(x)

def closed_neighbors(G,v):
    """
    Returns closed neighbors of a vertex
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
    v :     Vertex
            Integer of vertex            
           
    Returns
    -------
     :   List
     Returns closed neighbors of a vertex
    """    
    N = neighbors(G,v)
    N.append(v)
    return N
