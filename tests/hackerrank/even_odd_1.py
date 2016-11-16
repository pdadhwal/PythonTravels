def is_leap(year):
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    if divisible_by_100 and divisible_by_400:
        return True
    elif divisible_by_4:
        return True
    else:
        return False

