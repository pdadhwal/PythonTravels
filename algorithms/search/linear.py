def contains(collection, value):
    if collection is None:
        return False
    for member in collection:
        if member == value:
            return True
    return False
