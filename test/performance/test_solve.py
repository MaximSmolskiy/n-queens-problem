import pytest

from os import path
import sys
sys.path.append(path.abspath(path.join('..', '..', 'src')))
from solve import solve


@pytest.mark.parametrize('n', [10, 50, 100])
def test_solve(benchmark, n):
    benchmark(solve, n=n)
