import numpy as np

from os import path
import sys
sys.path.append(path.abspath(path.join('..', '..', 'src')))
from solve import solve


def test_solve():
    for n in range(1, 11):
        board = solve(n)

        if n in [2, 3]:
            assert np.sum(board) == n - 1
        else:
            assert np.sum(board) == n

        for row in range(n):
            assert np.sum(board[row, :]) <= 1

        for col in range(n):
            assert np.sum(board[:, col]) <= 1

        for diag in range(n):
            assert np.sum(board.diagonal(diag)) <= 1
            assert np.sum(board.diagonal(-diag)) <= 1

            assert np.sum(np.fliplr(board).diagonal(diag)) <= 1
            assert np.sum(np.fliplr(board).diagonal(-diag)) <= 1
