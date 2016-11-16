from datetime import datetime
import pytest
from algorithms import insertion_sort


class TestInsertionSort:
    @pytest.fixture
    def unsorted_list(self):
        return [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]

    @pytest.fixture
    def sorted_list(self):
        return list(range(1, 16))

    @pytest.fixture
    def empty_list(self):
        return []

    def test_asc_empty_list(self, empty_list):
        insertion_sort.asc(empty_list)

        assert 0 == len(empty_list)

    def test_desc_empty_list(self, empty_list):
        insertion_sort.desc(empty_list)

        assert 0 == len(empty_list)

    def test_asc_none(self):
        coll = None
        insertion_sort.asc(coll)

        assert coll is None

    def test_desc_none(self):
        coll = None
        insertion_sort.desc(coll)

        assert coll is None

    def test_desc_unsorted_list(self, unsorted_list):
        insertion_sort.desc(unsorted_list)

        for i in range(1, 17):
            assert unsorted_list[i - 1] == 16 - i + 1

    def test_asc_unsorted_list(self, unsorted_list):
        insertion_sort.asc(unsorted_list)

        for i in range(1, 16):
            assert unsorted_list[i - 1] == i
