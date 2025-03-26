import pytest
from max_in_range import max_in_range


@pytest.mark.parametrize('array, start, stop, expected_result', [
    ([3, 7, 2, 9, 4], 1, 3, 3),
    ([3, 7, 2, 9, 4], 1, 4, 3),
    ([1, 2, 3, 4, 5, 6], 0, 5, 5),
    ([6, 5, 4, 3, 2, 1], 0, 5, 0),
    ([1, 1, 1, 1, 1, 1], 2, 5, 2)

])
def test_max_in_range_positive(array, start, stop, expected_result):
    assert max_in_range(array, start, stop) == expected_result


@pytest.mark.parametrize('array, start, stop, expected_result', [
    (['1,2,3,4,5'], 1, 5, ValueError),
    ([6, 5, 4, 3, 2, 1], -1, 5, ValueError),
    (('1, 2, 3, 4, 5'), 2, 4, TypeError),
    ([], 1, 2, ValueError)

])
def test_max_in_range_negative(array, start, stop, expected_result):
    with pytest.raises(expected_result):
        max_in_range(array, start, stop)


@pytest.mark.parametrize('array, start, stop, expected_result', [
    ([1, 2], 0, 1, 1),
    ([0, 0], 0, 1, 0)

])
def test_max_in_range_limit(array, start, stop, expected_result):
    assert max_in_range(array, start, stop) == expected_result
