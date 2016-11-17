"""
    MergeSort implementation in Python
"""


def asc(a_list):
    if a_list is None:
        return
    """merge sort array in place."""
    copy = a_list
    __merge_sort(copy, a_list, 0, len(a_list))


def __merge_sort(a_list, result, start, end):
    """Merge sort array in memory with given range."""
    if end - start < 2:
        return
    if end - start == 2:
        if result[start] > result[start + 1]:
            result[start], result[start + 1] = result[start + 1], result[start]
        return

    mid = (end + start) // 2
    __merge_sort(result, a_list, start, mid)
    __merge_sort(result, a_list, mid, end)

    # merge array left- and right- side
    i = start
    j = mid
    idx = start
    while idx < end:
        if j >= end or (i < mid and a_list[i] < a_list[j]):
            result[idx] = a_list[i]
            i += 1
        else:
            result[idx] = a_list[j]
            j += 1

        idx += 1
