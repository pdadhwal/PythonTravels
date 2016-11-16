from algorithms import insertion_sort
import random


class TestInsertionSort:
    def test_empty_asc(self):
        insertion_sort.asc([])

    def test_none_asc(self):
        insertion_sort.asc(None)

    def test_for_different_input_sizes_asc(self):
        """Insertion sort is slow on inputs of large sizes"""
        for size in range(1, 50):
            c = [random.randint(1, 1000) for _ in range(size)]

            copy = c

            # sort using mergeSort and using builtin sort
            insertion_sort.asc(c)
            copy.sort()

            assert c == copy

    def test_empty_desc(self):
        insertion_sort.desc([])

    def test_none_desc(self):
        insertion_sort.desc(None)

    def test_for_different_input_sizes_desc(self):
        """Insertion sort is slow on inputs of large sizes"""
        for size in range(1, 50):
            c = [random.randint(1, 1000) for _ in range(size)]

            copy = c

            # sort using mergeSort and using builtin sort
            insertion_sort.desc(c)
            copy.sort(reverse=True)

            assert c == copy
