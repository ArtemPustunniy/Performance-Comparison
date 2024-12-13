import pytest


@pytest.mark.benchmark(group="string_concat")
@pytest.mark.parametrize("method", ["plus_equals", "join"])
def test_string_concat(benchmark, method):
    """
    Benchmark test for measuring the performance of string concatenation methods.

    Parameters:
    ----------
    benchmark : pytest_benchmark.fixture.BenchmarkFixture
        A pytest fixture for benchmarking the execution of a code block.
    method : str
        The method used to concatenate strings. Options are:
        - "plus_equals": Concatenation using the `+=` operator.
        - "join": Concatenation using the `str.join` method.

    Benchmark scenarios:
    --------------------
    1. `plus_equals`: Concatenates strings iteratively using the `+=` operator.
    2. `join`: Concatenates strings in bulk using `"".join()`.

    Test execution:
    ----------------
    The `benchmark` fixture measures the execution time required to concatenate
    a list of 10,000 strings using the specified method.

    Notes:
    ------
    - `plus_equals` is less efficient for large numbers of concatenations because
      it creates a new string object each time, leading to higher memory usage and
      slower performance.
    - `join` is generally faster as it optimizes memory usage by precomputing
      the size of the final string.
    """
    parts = ["string"] * 10_000

    if method == "plus_equals":
        def concat_plus_equals():
            result = ""
            for part in parts:
                result += part
            return result
        benchmark(concat_plus_equals)
    elif method == "join":
        benchmark(lambda: "".join(parts))
