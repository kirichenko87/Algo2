import pytest
from big_digit import big_digit


@pytest.mark.parametrize('array, expected_result', [
    ([1, 2, 3], [1, 2, 4]),
    ([1, 1, 1], [1, 1, 2]),
    ([1, 0, 0], [1, 0, 1]),
    ([1], [2])

])
def test_big_digit_positive(array, expected_result):
    assert big_digit(array) == expected_result


@pytest.mark.parametrize('array, expected_result', [
    ('1, 2, 3, 4, 5', TypeError),
    (1223, TypeError)
])
def test_big_digit_negative(array, expected_result):
    with pytest.raises(expected_result):
        big_digit(array)


@pytest.mark.parametrize('array, expected_result', [
    ([1], [2]),
    ([9], [1, 0])
])
def test_big_digit_limit(array, expected_result):
    assert big_digit(array) == expected_result
