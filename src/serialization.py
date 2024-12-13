import pytest
import pickle
import json
import msgpack


@pytest.mark.benchmark(group="serialization")
@pytest.mark.parametrize("format", ["pickle", "json", "msgpack"])
@pytest.mark.parametrize("size", [1_000, 1_000_000, 10_000_000])
def test_serialization(benchmark, format, size):
    """
    Benchmark test for measuring the performance of data serialization.

    Parameters:
    ----------
    benchmark : pytest_benchmark.fixture.BenchmarkFixture
        A pytest fixture for benchmarking the execution of a code block.
    format : str
        The serialization format to use. Options are:
        - "pickle": Python's built-in binary serialization format.
        - "json": Text-based serialization format.
        - "msgpack": Compact binary serialization format.
    size : int
        The size of the data to serialize, in bytes.

    Benchmark scenarios:
    --------------------
    1. `pickle`: Serializes a dictionary using Python's `pickle.dumps`.
    2. `json`: Serializes a dictionary using `json.dumps`.
    3. `msgpack`: Serializes a dictionary using `msgpack.packb`.

    Test execution:
    ----------------
    The `benchmark` fixture measures the execution time required to serialize
    a dictionary containing repeated string values for each specified format
    and data size.
    """
    data = {"key": "value" * (size // 10)}

    if format == "pickle":
        benchmark(lambda: pickle.dumps(data))
    elif format == "json":
        benchmark(lambda: json.dumps(data))
    elif format == "msgpack":
        benchmark(lambda: msgpack.packb(data))


@pytest.mark.benchmark(group="deserialization")
@pytest.mark.parametrize("format", ["pickle", "json", "msgpack"])
@pytest.mark.parametrize("size", [1_000, 1_000_000, 10_000_000])
def test_deserialization(benchmark, format, size):
    """
    Benchmark test for measuring the performance of data deserialization.

    Parameters:
    ----------
    benchmark : pytest_benchmark.fixture.BenchmarkFixture
        A pytest fixture for benchmarking the execution of a code block.
    format : str
        The serialization format to use. Options are:
        - "pickle": Python's built-in binary serialization format.
        - "json": Text-based serialization format.
        - "msgpack": Compact binary serialization format.
    size : int
        The size of the serialized data to deserialize, in bytes.

    Benchmark scenarios:
    --------------------
    1. `pickle`: Deserializes a dictionary using Python's `pickle.loads`.
    2. `json`: Deserializes a dictionary using `json.loads`.
    3. `msgpack`: Deserializes a dictionary using `msgpack.unpackb`.

    Test execution:
    ----------------
    The `benchmark` fixture measures the execution time required to deserialize
    a serialized dictionary for each specified format and data size.
    """
    data = {"key": "value" * (size // 10)}

    if format == "pickle":
        serialized = pickle.dumps(data)
        benchmark(lambda: pickle.loads(serialized))
    elif format == "json":
        serialized = json.dumps(data)
        benchmark(lambda: json.loads(serialized))
    elif format == "msgpack":
        serialized = msgpack.packb(data)
        benchmark(lambda: msgpack.unpackb(serialized))
