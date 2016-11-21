from algorithms.search import linear
import random


class TestLinearSearch:
    def test_empty_list(self):
        assert not linear.contains([], 100)

    def test_none_list(self):
        assert not linear.contains(None, 100)

    def test_return_true(self):
        assert linear.contains([1, 4], 4)

    def test_return_false(self):
        assert not linear.contains([1, 2], 3)

    def test_a_large_lists(self):
        for size in range(1, 100):
            c = [random.randint(1, 1000) for _ in range(size)]
            assert linear.contains(c, c[size-1])
