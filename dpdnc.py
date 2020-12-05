"""
The version combining dynamic programming and divide and conquer approaches allowing one to solve the problem with a linear space complexity
"""
import sys
import ed as ED

from dyna import dyna_ed
from dyna import max3


def spaceeff_dyna(x, y, c):
    """
    Find the LCS_length end value with a linear space forward algorithm
    """
    n = len(y)
    m = len(x)
    for i in range(1, m + 1):
        c[0][1] = 0
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[j][1] = c[j - 1][0] + 1
            else:
                ctop = c[j][0]
                cleft = c[j - 1][1]
                ctopleft = c[j - 1][0]

                c[j][1], d = max3(ctopleft, ctop, cleft)
        for k in range(len(c)):
            c[k][0] = c[k][1]


def back_spaceeff_dyna(x, y, c):
    """
    Find the LCS_length end value with a linear space backward algorithm
    """
    n = len(y)
    m = len(x)
    for i in range(m - 1, -1, -1):
        c[n][1] = 0
        for j in range(n - 1, -1, -1):
            if x[i] == y[j]:
                c[j][1] = c[j + 1][0] + 1
            else:
                cbottom = c[j][0]
                cright = c[j + 1][1]
                cbottomright = c[j + 1][0]

                c[j][1], d = max3(cbottomright, cbottom, cright)
        for k in range(len(c)):
            c[k][0] = c[k][1]


def dpdnc_ed_calcq(buffer_forward: list, buffer_backward: list):
    """
    Finding q : index maximizing buffer_forward[i][1] + buffer_backward[i][1]
    """
    q = 0
    mx = buffer_forward[0][1] + buffer_backward[0][1]
    for i in range(1, len(buffer_forward)):
        t = buffer_forward[i][1] + buffer_backward[i][1]
        if t > mx:
            mx = t
            q = i
    return q


def dpdnc_ed(x, y, ed, shifti=0, shiftj=0):
    """
    Compute with a divide and conquer and a DP approach the ED
    """
    m = len(x)
    n = len(y)
    if m <= 2 or n <= 2:
        dyna_ed(x, y, ed, shifti, shiftj)
    else:
        # Calling space efficient LCS
        buffer_forward = [[0, 0] for _ in range(len(y) + 1)]
        buffer_backward = [[0, 0] for _ in range(len(y) + 1)]
        spaceeff_dyna(x[:m // 2], y, buffer_forward)
        back_spaceeff_dyna(x[m // 2:][::-1], y[::-1], buffer_backward)

        # Finding q
        q = dpdnc_ed_calcq(buffer_forward, buffer_backward)

        # Recursive call
        dpdnc_ed(
            x[n // 2 + 1:], y[q + 1:], ed, shifti + n // 2 + 1, shiftj + q + 1)
        dpdnc_ed(
            x[: n // 2], y[:q], ed, shifti, shiftj)


def dpdnc(x, y):
    """
    divide and conquer LCS algorithm
    """
    ed = ED.EdData(x, y)
    dpdnc_ed(x, y, ed)
    ed.complete_path()
    ed.complete_reverse()
    ed.complete_indexes()
    return ed

def test_set():
    lettre=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','e','p','q','r','s','t','u','v','w','x','y','z']
    texte1=''
    texte2=''
    number_lettre1=random.randint(2,100)
    for i in range(number_lettre1):
        rank= random.randint(0, 25)
        texte1+=lettre[rank]
    number_lettre2=random.randint(2,5)
    for i in range(number_lettre2):
        rank= random.randint(0, 25)
        texte2+=lettre[rank]
    return texte1, texte2


######## Database protein ########
import pandas as pd
colonne=['first','second','third']
data = pd.read_csv('proteine.csv',names=colonne, skiprows=4)
valeur=data['third']

        

if __name__ == "__main__":
    # x = "hell"
    # y = "helico"
    
    ##### For the Set test ####
    # for i in range(0,100):
    #     x,y=test_set()
    #     dpdnc(x, y).show(True)
    
    ##### For the Database ####
    for i in range(len(valeur)):
        x=valeur[i]
        if i < len(valeur)-1:
            y=valeur[i+1]
        dpdnc(x, y).show(True)
