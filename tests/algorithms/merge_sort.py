import random

from algorithms.sort import merge


class TestAscMergeSort:
    def test_empty(self):
        merge.asc([])

    def test_none(self):
        merge.asc(None)

    def test_for_different_input_sizes(self):
        for size in range(1, 500):
            c = [random.randint(1, 1000) for _ in range(size)]

            copy = c

            # sort using mergeSort and using builtin sort
            merge.asc(c)
            copy.sort()

            assert c == copy
