import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors



def is_independent(G,S):
    for v in S:
        if list(set(S) & set(neighbors(G, v))) != []:
            return False
        return True
    
def maximum_independent_set(G):
    n = len(V(G))
    for k in range(n-1,1, -1):
        for s in combinations(V(G),k):
            if is_independent(G,list(s)) == True:
                return list(s)
            
def independence_number(G):
    return len(maximum_independent_set(G))

