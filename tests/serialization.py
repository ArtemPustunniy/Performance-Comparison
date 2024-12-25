import pytest
import pickle
import json
import msgpack


def pickle_serialize(data):
    return pickle.dumps(data)


def json_serialize(data):
    return json.dumps(data)


def msgpack_serialize(data):
    return msgpack.packb(data)


def pickle_deserialize(serialized):
    return pickle.loads(serialized)


def json_deserialize(serialized):
    return json.loads(serialized)


def msgpack_deserialize(serialized):
    return msgpack.unpackb(serialized)


@pytest.mark.benchmark(group="serialization")
@pytest.mark.parametrize("serializer", [pickle_serialize, json_serialize, msgpack_serialize])
@pytest.mark.parametrize("size", [1_000, 1_000_000, 10_000_000])
def test_serialization(benchmark, serializer, size):
    """
    Benchmark test for measuring the performance of data serialization.

    Parameters:
    ----------
    benchmark : pytest_benchmark.fixture.BenchmarkFixture
        A pytest fixture for benchmarking the execution of a code block.
    serializer : callable
        The serialization function to use.
    size : int
        The size of the data to serialize, in bytes.
    """
    data = {"key": "value" * (size // 10)}
    benchmark(lambda: serializer(data))


@pytest.mark.benchmark(group="deserialization")
@pytest.mark.parametrize("serializer, deserializer", [
    (pickle_serialize, pickle_deserialize),
    (json_serialize, json_deserialize),
    (msgpack_serialize, msgpack_deserialize)
])
@pytest.mark.parametrize("size", [1_000, 1_000_000, 10_000_000])
def test_deserialization(benchmark, serializer, deserializer, size):
    """
    Benchmark test for measuring the performance of data deserialization.

    Parameters:
    ----------
    benchmark : pytest_benchmark.fixture.BenchmarkFixture
        A pytest fixture for benchmarking the execution of a code block.
    serializer : callable
        The serialization function to use.
    deserializer : callable
        The deserialization function to use.
    size : int
        The size of the serialized data to deserialize, in bytes.
    """
    data = {"key": "value" * (size // 10)}
    serialized = serializer(data)
    benchmark(lambda: deserializer(serialized))
