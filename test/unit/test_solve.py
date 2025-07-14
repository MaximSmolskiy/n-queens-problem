import numpy as np
import pytest

from os import path
import sys
sys.path.append(path.abspath(path.join(__file__, '..', '..', '..', 'src')))
from solve import solve


@pytest.mark.parametrize('n', range(1, 11))
def test_solve(n):
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
