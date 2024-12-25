import pytest
import numpy as np


def create_with_list_comprehension(size):
    return [x for x in range(size)]


def create_with_for_loop(size):
    result = []
    for x in range(size):
        result.append(x)
    return result


def create_with_numpy(size):
    return np.arange(size).tolist()


@pytest.mark.benchmark(group="list_creation")
@pytest.mark.parametrize("method", [create_with_list_comprehension, create_with_for_loop, create_with_numpy])
def test_list_creation(benchmark, method):
    """
    Benchmark test for measuring the performance of list creation using different methods.

    Parameters:
    ----------
    benchmark : pytest_benchmark.fixture.BenchmarkFixture
        A pytest fixture for benchmarking the execution of a code block.
    method : callable
        The function used to create a list.
    """
    size = 10_000
    benchmark(lambda: method(size))
