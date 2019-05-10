import networkx as nx
from functions.local_properties import neighbors

def V(G):
    """
    Returns the verticies of a graph
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
           
    Returns
    -------
     :   set
     Returns list of vertices in a graph
    """
    return nx.nodes(G) 

def E(G):
    """
    Returns the edges of a graph
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
           
    Returns
    -------
     :   set
     Returns list of edges in a graph
    """
    return nx.edges(G)  

def n(G):
    """
    Returns the number of verticies of a graph
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
           
    Returns
    -------
     :   integer
     Returns number of verticies
    """
    return len(V(G)) 

def m(G):
    """
    Returns the number of edges (size) of a graph
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
           
    Returns
    -------
     :   integer
     Returns number of edges
    """
    return len(E(G))    


#############################################################################

#returns the length of neighbors
def degree(G,v):
    """
    Returns the length of neighbors of a given point
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
    v :     Vertex
           
    Returns
    -------
     :   integer
     Returns length of neighbors of a vertex
    """
    return len(neighbors(G,v))

#print(neighbors(G, '5'))

#returns the degree_sequence
def degree_sequence(G):
    """
    Returns the degree_sequence
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
           
    Returns
    -------
     :   Set
     Returns degree Sequence of point
    """
    D = [degree(G,v) for v in V(G)]
    D.sort(reverse = True)
    return D

#returns the maximum degree
def maxmimum_degree(G):
    """
    Returns the Maximum Degree of a Graph
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
           
    Returns
    -------
     :   Integer
     Returns Maximum Degree of a Networkx Graph
    """
    return degree_sequence(G)[0]

def minimum_degree(G):
    """
    Returns the Minimum Degree of a Graph
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
           
    Returns
    -------
     :   Integer
     Returns Minimun Degree of a Networkx Graph
    """    
    return degree_sequence(G)[-1]

def avg_degree(G):
        """
    Returns the the average of the degree
    
    Parameters
    ----------
    G :     Networkx graph
            Undirected graph
           
    Returns
    -------
     :   Integer
     Returns the average of the degree
    """
    return sum(degree_sequence(G)) / n(G)


#############################################################################


def distance_array(G,v):
    N = [[v]]
    Obs = [v]
    i = 1
    while set(Obs) != set(V(G)):
        print(f'Iteration {i} = {N}')
        temp_neighbors = []
        for x in N[-1]:
            for y in neighbors(G,x):
                if y not in Obs:
                    temp_neighbors.append(y)
                    Obs.append(y)
        N.append(temp_neighbors)
        return N

def distance(G,v,w):
    D = distance_array(G,v)
    for i in range(len(D)):
        if w in D[i]:
            return i
        
#############################################################################

#returns the center of the graph
def eccentricity(G,v):
    return len(distance_array (G,v)) - 1

#returns the radius
def radius(G):
    return min([eccentricity(G,v) for v in V(G)])

#returns the diameter of the graph
def diameter(G):
    return max([eccentricity(G,v) for v in V(G)])

