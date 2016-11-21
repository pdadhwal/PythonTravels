from algorithms.search import binary as binary_search


class TestBinarySearch:
    def test_none(self):
        assert not binary_search.contains(None, 1)

    def test_empty(self):
        assert not binary_search.contains([], 1)

    def test_should_return_false(self):
        assert not binary_search.contains([1, 2, 3, 4], 5)

    def test_should_return_true_odd_num_elements(self):
        assert binary_search.contains([1, 2, 3, 4, 5], 1)

    def test_should_return_true_even_num_elements(self):
        assert binary_search.contains([1, 2, 3, 4], 1)
