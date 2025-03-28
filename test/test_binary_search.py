import pytest
from binary_search import binary_search


@pytest.mark.parametrize('array, target, expected_result', [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 1),
    ([1, 3, 5, 7, 9], 5, 2)
])
def test_binary_search_positive(array, target, expected_result):
    assert binary_search(array, target) == expected_result


@pytest.mark.parametrize('array, target, expected_result', [
    ('123', 4, TypeError),
    (123, 3, TypeError),
    ([1, 2, 3, 4], '3', TypeError)

])
def test_binary_search_negative(array, target, expected_result):
    with pytest.raises(expected_result):
        binary_search(array, target)


@pytest.mark.parametrize('array, target, expected_result', [
    ([1], 1, 0),
    ([0], 0, 0)
])
def test_binary_search_limit(array, target, expected_result):
    assert binary_search(array, target) == expected_result
