import random
from algorithms import merge_sort


class TestAscMergeSort:
    def test_empty(self):
        merge_sort.asc([])

    def test_none(self):
        merge_sort.asc(None)

    def test_for_different_input_sizes(self):
        for size in range(1, 500):
            c = [random.randint(1, 1000) for _ in range(size)]

            copy = c

            # sort using mergeSort and using builtin sort
            merge_sort.asc(c)
            copy.sort()

            assert c == copy
