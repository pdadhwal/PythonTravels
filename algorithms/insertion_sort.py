def asc(a_list):
    """Sorts the input list (in place) in ascending order"""
    if a_list is None:
        return

    if len(a_list) == 0:
        return

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0:
            if a_list[position - 1] > current_value:
                a_list[position - 1], a_list[position] = a_list[position], a_list[position - 1]
            position -= 1


def desc(a_list):
    """Sorts the input list (in place) in descending order"""
    if a_list is None:
        return

    if len(a_list) == 0:
        return

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0:
            if a_list[position - 1] < current_value:
                a_list[position - 1], a_list[position] = a_list[position], a_list[position - 1]
            position -= 1
