"""
An approximated version of the classical dynamic programming approach where one fills only a stripe of size k around the diagonal of the matrix.
"""
import sys
import ed as ED
from dyna import max3


def approximated_dp_ed(x, y, k, ed):
    """
    Compute the ED with an approximated divide and conquer LCS algorithm
    """
    if not (k < len(x) and k < len(y)) or k < 1:
        raise Exception('BAD K')

    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n)] for _ in range(m)]

    diff = m - n

    left = - k // 2
    right = k // 2 + k % 2

    if diff > 0:  # m > n -> x longer than y
        left -= diff
    else:  # m > n -> y longer than x
        right += -diff  # (-) because diff < 0

    # building b and c
    for i in range(m):
        for j in range(max(1, left), min(n, right)):
            if x[i] == y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                b[i][j] = 0  # TOPLEFT
            else:
                ctop = c[i][j + 1]
                cleft = c[i + 1][j]
                ctopleft = c[i][j]

                c[i + 1][j + 1], b[i][j] = max3(ctopleft, ctop, cleft)

        left += 1
        right += 1

    # building answer

    i = m - 1
    j = n - 1

    while i >= 0 and j >= 0:
        ed.add_marker(i, j)
        if b[i][j] == 0:  # TOPLEFT
            i -= 1
            j -= 1
        elif b[i][j] == 1:  # TOP
            i -= 1
        else:
            j -= 1

    while i >= 0 or j >= 0:
        if i >= 0:
            ed.add_marker(i, j)
            i -= 1
        if j >= 0:
            ed.add_marker(i, j)
            j -= 1

    ed.add_marker(i, j)


def approximated_dp(x, y, k=1):
    """
    approximated divide and conquer LCS algorithm
    """
    ed = ED.EdData(x, y)
    approximated_dp_ed(x, y, k, ed)
    ed.complete_path()
    ed.complete_reverse()
    ed.complete_indexes()
    return ed


if __name__ == "__main__":
    x = "helico"
    y = "hell"

    approximated_dp(x, y).show(True)
