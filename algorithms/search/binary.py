def contains(collection, value):
    """assumes that the collection is already sorted """
    if collection is None:
        return False

    low = 0
    high = len(collection) - 1

    while low <= high:
        mid = (low + high) // 2

        if value < collection[mid]:
            high = mid - 1
        elif value > collection[mid]:
            low = mid + 1
        else:
            return True
    return False
