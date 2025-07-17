import numpy as np
import scipy.optimize as opt


def solve(n):
    c = -np.ones(n * n)
    integrality = np.ones(n * n)
    bounds = opt.Bounds(lb=0, ub=1)

    A = []
    for row in range(n):
        board = np.zeros((n, n))
        board[row, :] = 1
        A.append(board.ravel())

    for col in range(n):
        board = np.zeros((n, n))
        board[:, col] = 1
        A.append(board.ravel())

    ones = np.ones((n, n))
    for diag in range(n):
        A.append(np.diag(v=ones.diagonal(diag), k=diag).ravel())
        A.append(np.diag(v=ones.diagonal(-diag), k=-diag).ravel())

        A.append(np.fliplr(np.diag(v=ones.diagonal(diag), k=diag)).ravel())
        A.append(np.fliplr(np.diag(v=ones.diagonal(-diag), k=-diag)).ravel())

    constraints = opt.LinearConstraint(A=A, ub=1)

    res = opt.milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints)
    return res.x.round().astype(bool).reshape((n, n))
