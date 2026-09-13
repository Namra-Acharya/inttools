def count_digits(x: int) -> int:
    """
    Return the number of decimal digits in an integer.

    The sign is ignored.

    Examples:
        count_digits(58392)   -> 5
        count_digits(0)       -> 1
        count_digits(-58392)  -> 5
    """
    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError("count_digits() requires an integer")

    x = abs(x)

    if x == 0:
        return 1

    count = 0

    while x:
        x //= 10
        count += 1

    return count


def remove_last(x: int) -> int:
    """
    Remove the last decimal digit from an integer.

    Examples:
        remove_last(58392)   -> 5839
        remove_last(-58392)  -> -5839
        remove_last(5)       -> 0
        remove_last(0)       -> 0
    """
    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError("remove_last() requires an integer")

    sign = -1 if x < 0 else 1

    return sign * (abs(x) // 10)


def remove_first(n: int) -> str:
    """
    Remove the first decimal digit from an integer
    while preserving leading zeros.

    Examples:
        remove_first(58392)   -> "8392"
        remove_first(102)     -> "02"
        remove_first(1002)    -> "002"
        remove_first(-58392)  -> "-8392"
        remove_first(-102)    -> "-02"
        remove_first(7)       -> "0"
        remove_first(0)       -> "0"
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("remove_first() requires an integer")

    sign = "-" if n < 0 else ""
    digits = str(abs(n))

    if len(digits) == 1:
        return "0"

    result = digits[1:]

    if result.strip("0") == "":
        if sign == "-" or len(result) <= 2:
            return "0"
        return result

    return sign + result