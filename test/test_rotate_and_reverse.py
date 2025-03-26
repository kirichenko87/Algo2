import pytest
from rotate_and_reverse import rotate_and_reverse


@pytest.mark.parametrize('array, value, expected_result', [
    ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
    ([4, 2, 1, 5], 2, [2, 4, 5, 1]),
    ([1, 2, 3, 4, 5], 2, [3, 2, 1, 5, 4]),
    ([1, 2, 3], 1, [2, 1, 3])

])
def test_rotate_and_reverse_positive(array, value, expected_result):
    assert rotate_and_reverse(array, value) == expected_result


@pytest.mark.parametrize('array, value, expected_result', [
    ('1,2,3,4,5', 1, TypeError),
    ([1, 2, 3], -4, ValueError),
    ([], 1, ValueError)

])
def test_rotate_and_reverse_negative(array, value, expected_result):
    with pytest.raises(expected_result):
        rotate_and_reverse(array, value)


@pytest.mark.parametrize('array, value, expected_result', [
    ([0], 1, [0]),
    ([-1, 2, 3, 1], 1, [3, 2, -1, 1])
])
def test_rotate_and_reverse_limit(array, value, expected_result):
    assert rotate_and_reverse(array, value) == expected_result
