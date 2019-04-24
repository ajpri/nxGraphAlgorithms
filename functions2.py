

import networkx as nx


#G = nx.read_edgelist('G.txt')
G = nx.read_edgelist('testG4.txt')
#G = nx.read_edgelist('colorG.txt')


nx.draw(G)

#print(nx.nodes(G))

def V(G):
    return nx.nodes(G)

def E(G):
    return nx.edges(G)

def n(G):
    return len(V(G))

def m(G):
    return len(E(G))

def neighbors(G,v):
    return list(nx.neighbors(G,v)) #print(list(nx.neighbors(G,'5')))

def degree(G,v):
    return len(neighbors(G,v))

#print(neighbors(G, '5'))
    
def degree_sequence(G):
    D = [degree(G,v) for v in V(G)]
    D.sort(reverse = True)
    return D

def maxmimum_degree(G):
    return degree_sequence(G)[0]

def minimim_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree_sequence(G)) / n(G)

#G = nx.read_edgelist('G.txt')

#nx.draw(G)

##################################################

#H = nx.erdos_renyi_graph(32, .14)
#nx.draw(H)

#H = nx.davis_southern_women_graph()
#nx.draw(H)

#print(f'minimum degree: {minimum_degree(H)}')
#print('')

#print(f'maximum degree: {maximum_degree(H)}')
#print('')

#print(f'average degree: {avg_degree(H)}')
#print('')

#print(f'V(G): = {V(H)}')
#print('')

#print(f'E(G): = {E(H)}')

##################################################

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
        
def eccentricity(G,v):
    return len(distance_array (G,v)) - 1

def radius(G):
    return min([eccentricity(G,v) for v in V(G)])

def diameter(G):
    return max([eccentricity(G,v) for v in V(G)])

def graph_center(G):
    return [v for v in V(G)
            if eccentricity(G,v) == radius(G)]

#print(graph_center(G))


#***********************************************
#4/3/19

def delete_first_term(L):
    L.pop(0)    #delete_first_term(L)
    return None

#L = [4,3,3,2,2,2]
#delete_first_term(L)
#print(L)

def havel_hakimi_derivative(L):
    d_1 = L[0]
    L.pop(0)
    for i in range(d_1):
        L[i] -= 1
    L.sort(reverse = True)
    return None

#L = [3,3,3,2,2,1]
#havel_hakimi_derivative(L)
#print(L)
#havel_hakimi_derivative(L)
#print(L)


def havel_hakimi_process(L, show = False):
    assert len(L) != 0, 'List connot be empty'
    if show == True:
        print(L)
    while L[0] > 0:
        havel_hakimi_derivative(L)
        if show == True:
            print(L)
    return None

#L = [3,3,3,2,2,1]
#havel_hakimi_process(L, show=True)
#print(L)

def is_graphic(L):
    havel_hakimi_process(L)
    return sum(L) ==0


def residue(G):
    L = degree_sequence(G)
    havel_hakimi_process(L)
    return len(L)

#print(residue(G))

#***********************************************
#4/8/19















