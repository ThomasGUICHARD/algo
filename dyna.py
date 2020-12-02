"""
The classic algorithm based on dynamic programming. The algorithm is similar to the LCS problem
"""
import sys
import ed as ED


def max3(a, b, c):
    if a >= b:
        if a >= c:
            return a, 0  # a > b & a > c
        else:
            return c, 2  # c > a > b
    else:
        if b >= c:
            return b, 1  # b > a & b > c
        else:
            return c, 2  # c > b > a


def dyna_ed_buildbc(m, n, x, y):
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n)] for _ in range(m)]

    # building b and c
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                b[i][j] = 0  # TOPLEFT
            else:
                ctop = c[i][j + 1]
                cleft = c[i + 1][j]
                ctopleft = c[i][j]

                c[i + 1][j + 1], b[i][j] = max3(ctopleft, ctop, cleft)

    return b, c


def dyna_ed(x, y, ed, shifti=0, shiftj=0):
    """
    LCS algorithm with non linear space complexity
    """

    m = len(x)
    n = len(y)

    b, c = dyna_ed_buildbc(m, n, x, y)

    # building answer

    i = m - 1
    j = n - 1

    while i >= 0 and j >= 0:
        ed.add_marker(i + shifti, j + shiftj)
        if b[i][j] == 0:  # TOPLEFT
            i -= 1
            j -= 1
        elif b[i][j] == 1:  # TOP
            i -= 1
        else:
            j -= 1

    while i >= 0 or j >= 0:
        if i >= 0:
            ed.add_marker(i + shifti, j + shiftj)
            i -= 1
        if j >= 0:
            ed.add_marker(i + shifti, j + shiftj)
            j -= 1

    ed.add_marker(i + shifti, j + shiftj)


def dyna(x, y):
    """
    divide and conquer LCS algorithm
    """
    ed = ED.EdData(x, y)
    dyna_ed(x, y, ed)
    ed.complete_path()
    ed.complete_reverse()
    ed.complete_indexes()
    return ed


if __name__ == "__main__":
    x = "helico"
    y = "hell"

    ed = dyna(x, y)
    ed.show(True)
