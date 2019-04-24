


def Havel_hakimi_dervate(L):
    d_1 = L[0]
    L.pop(0)
    for i in range(d_1):
        L[i] -=1
    L.sort(reverse=True)
    return None

