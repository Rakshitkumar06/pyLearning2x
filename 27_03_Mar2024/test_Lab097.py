# Fixture ( Concept in python) , pytest
# You can use the Fixture 1. setup, provide, teardown resource in your Testcases.
# pass some of the data to other testcases you can use the fixture.

import pytest


@pytest.fixture()
def sample_data():
    data = [1, 2, 3, 4, 5]
    return data


def test_num1_sample_data_to_injected(sample_data):
    assert len(sample_data) == 5
