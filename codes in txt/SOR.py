# successive over-relaxation

def column(m, c):
    return [m[i][c] for i in range(len(m))]


def row(m, r):
    return m[r][:]


def height(m):
    return len(m)


def width(m):
    return len(m[0])

def sor(m, w=1.25, x0=None, eps=1e-5, max_iteration=100):
    """
    Parameters
    ----------
    m  : list of list of floats : coefficient matrix
    w  : float : weight
    x0 : list of floats : initial guess
    eps: float : error tolerance
    max_iteration: int

    Returns
    -------
    list of floats
        solution to the system of linear equation

    Raises
    ------
    ValueError
        Solution does not converge
    """
    n = height(m)
    x0 = [0] * n if x0 == None else x0
    x1 = x0[:]

    for __ in range(max_iteration):
        for i in range(n):
            s = sum(-m[i][j] * x1[j] for j in range(n) if i != j)
            x1[i] = w * (m[i][n] + s) / m[i][i] + (1 - w) * x0[i]
        if all(abs(x1[i] - x0[i]) < eps for i in range(n)):
            return x1
        x0 = x1[:]
    raise ValueError('Solution does not converge')


if __name__ == '__main__':
    m = [[3,-1,1,-1], [-1,3,-1,7], [1,-1,3,-7]]
    print(sor(m))

# author: Worasait Suwannik
# date: May 2015
