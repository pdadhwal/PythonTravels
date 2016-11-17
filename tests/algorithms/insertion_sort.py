import random

from algorithms.sort import insertion


class TestInsertionSort:
    def test_empty_asc(self):
        insertion.asc([])

    def test_none_asc(self):
        insertion.asc(None)

    def test_for_different_input_sizes_asc(self):
        """Insertion sort is slow on inputs of large sizes"""
        for size in range(1, 50):
            c = [random.randint(1, 1000) for _ in range(size)]

            copy = c

            # sort using mergeSort and using builtin sort
            insertion.asc(c)
            copy.sort()

            assert c == copy

    def test_empty_desc(self):
        insertion.desc([])

    def test_none_desc(self):
        insertion.desc(None)

    def test_for_different_input_sizes_desc(self):
        """Insertion sort is slow on inputs of large sizes"""
        for size in range(1, 50):
            c = [random.randint(1, 1000) for _ in range(size)]

            copy = c

            # sort using mergeSort and using builtin sort
            insertion.desc(c)
            copy.sort(reverse=True)

            assert c == copy
