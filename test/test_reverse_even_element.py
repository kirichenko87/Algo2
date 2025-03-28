import pytest
from reverse_even_elements import reverse_even_elements


@pytest.mark.parametrize('array, expected_result', [
    ([1, 2, 3, 4, 5, 6], [1, 6, 3, 4, 5, 2]),
    ([2, 4, 6, 8, 10], [10, 8, 6, 4, 2]),
    ([1, 2], [1, 2]),
    ([2, 1], [2, 1])
])
def test_reverse_even_elements_positive(array, expected_result):
    assert reverse_even_elements(array) == expected_result


@pytest.mark.parametrize('array, expected_result', [
    ('1, 2, 3', TypeError),
    (123, TypeError)
])
def test_reverse_even_elements(array, expected_result):
    with pytest.raises(expected_result):
        reverse_even_elements(array)


@pytest.mark.parametrize('array, expected_result', [
    ([2], [2]),
    ([1], [1])
])
def test_reverse_even_elements(array, expected_result):
    assert reverse_even_elements(array) == expected_result
