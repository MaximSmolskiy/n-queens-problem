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
        assert board.sum() == n - 1
    else:
        assert board.sum() == n

    for row in range(n):
        assert board[row, :].sum() <= 1

    for col in range(n):
        assert board[:, col].sum() <= 1

    for diag in range(n):
        assert board.diagonal(diag).sum() <= 1
        assert board.diagonal(-diag).sum() <= 1

        assert np.fliplr(board).diagonal(diag).sum() <= 1
        assert np.fliplr(board).diagonal(-diag).sum() <= 1
