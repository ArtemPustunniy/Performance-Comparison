import pytest
import numpy as np


@pytest.mark.benchmark(group="list_creation")
@pytest.mark.parametrize("method", ["list_comprehension", "for_loop", "numpy"])
def test_list_creation(benchmark, method):
    """
    Benchmark test for measuring the performance of list creation using different methods.

    Parameters:
    ----------
    benchmark : pytest_benchmark.fixture.BenchmarkFixture
        A pytest fixture for benchmarking the execution of a code block.
    method : str
        The method used to create a list. Options are:
        - "list_comprehension": Using a Python list comprehension.
        - "for_loop": Using a standard Python for loop to append elements to a list.
        - "numpy": Using NumPy's `arange` to generate the list.

    Benchmark scenarios:
    --------------------
    1. `list_comprehension`: Creates a list of integers from 0 to 9,999 using list comprehension.
    2. `for_loop`: Creates a list of integers from 0 to 9,999 by appending elements in a loop.
    3. `numpy`: Creates a NumPy array using `arange` and converts it to a list.

    Test execution:
    ----------------
    The `benchmark` fixture measures the execution time of the specified list creation method
    and compares performance across the three implementations.
    """
    size = 10_000

    if method == "list_comprehension":
        benchmark(lambda: [x for x in range(size)])
    elif method == "for_loop":
        def create_list():
            result = []
            for x in range(size):
                result.append(x)
            return result
        benchmark(create_list)
    elif method == "numpy":
        benchmark(lambda: np.arange(size).tolist())
