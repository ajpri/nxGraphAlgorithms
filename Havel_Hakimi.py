import networkx as nx
from functions.global_properties import *
G = nx.read_edgelist('graph_library/pan.txt')


def delete_first_term(L):
    L.pop(0)    #delete_first_term(L)
    return None

L = [4,3,3,2,2,2]
print(L)
delete_first_term(L)
print(L)

def havel_hakimi_derivative(L):
    d_1 = L[0]
    L.pop(0)
    for i in range(d_1):
        L[i] -= 1
    L.sort(reverse = True)
    return None


havel_hakimi_derivative(L)
print(L)


def havel_hakimi_process(L):
    while L[0] > 0:
        havel_hakimi_derivative(L)
    return None



def havel_hakimi_process(L, show = False):
    assert len(L) != 0, 'List connot be empty'
    if show == True:
        print(L)
    while L[0] > 0:
        havel_hakimi_derivative(L)
        if show == True:
            print(L)
    return None

havel_hakimi_process(L, show=True)


def is_graphic(L):
    havel_hakimi_process(L)
    return sum(L) ==0


def residue(G):
    L = degree_sequence(G)
    havel_hakimi_process(L)
    return len(L)

print('Residue:', residue(G))
