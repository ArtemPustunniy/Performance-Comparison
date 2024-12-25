import pytest


def concat_plus_equals(parts):
    result = ""
    for part in parts:
        result += part
    return result


def concat_join(parts):
    return "".join(parts)


@pytest.mark.benchmark(group="string_concat")
@pytest.mark.parametrize("method", [concat_plus_equals, concat_join])
def test_string_concat(benchmark, method):
    """
    Benchmark test for measuring the performance of string concatenation methods.

    Parameters:
    ----------
    benchmark : pytest_benchmark.fixture.BenchmarkFixture
        A pytest fixture for benchmarking the execution of a code block.
    method : callable
        The function used to concatenate strings. Options are:
        - concat_plus_equals: Concatenation using the `+=` operator.
        - concat_join: Concatenation using the `str.join` method.

    Benchmark scenarios:
    --------------------
    1. `concat_plus_equals`: Concatenates strings iteratively using the `+=` operator.
    2. `concat_join`: Concatenates strings in bulk using `"".join()`.

    Test execution:
    ----------------
    The `benchmark` fixture measures the execution time required to concatenate
    a list of 10,000 strings using the specified method.

    Notes:
    ------
    - `concat_plus_equals` is less efficient for large numbers of concatenations because
      it creates a new string object each time, leading to higher memory usage and
      slower performance.
    - `concat_join` is generally faster as it optimizes memory usage by precomputing
      the size of the final string.
    """
    parts = ["string"] * 10_000
    benchmark(lambda: method(parts))
