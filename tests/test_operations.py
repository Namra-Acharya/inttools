import pytest

from inttools import count_digits, remove_last, remove_first


# =========================
# count_digits()
# =========================

@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 1),
        (1, 1),
        (7, 1),
        (10, 2),
        (42, 2),
        (99, 2),
        (100, 3),
        (102, 3),
        (999, 3),
        (1000, 4),
        (58392, 5),
        (-1, 1),
        (-7, 1),
        (-42, 2),
        (-102, 3),
        (-58392, 5),
    ],
)
def test_count_digits(value, expected):
    assert count_digits(value) == expected


# =========================
# remove_last()
# =========================

@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0),
        (1, 0),
        (7, 0),
        (10, 1),
        (42, 4),
        (100, 10),
        (102, 10),
        (1002, 100),
        (58392, 5839),
        (5907, 590),
        (-1, 0),
        (-7, 0),
        (-10, -1),
        (-42, -4),
        (-100, -10),
        (-102, -10),
        (-1002, -100),
        (-58392, -5839),
        (-5907, -590),
    ],
)
def test_remove_last(value, expected):
    assert remove_last(value) == expected


# =========================
# remove_first()
# =========================

@pytest.mark.parametrize(
    "value, expected",
    [
        (0, "0"),
        (1, "0"),
        (7, "0"),
        (10, "0"),
        (42, "2"),
        (99, "9"),
        (100, "0"),
        (102, "02"),
        (1002, "002"),
        (58392, "8392"),
        (5907, "907"),
        (-1, "0"),
        (-7, "0"),
        (-10, "0"),
        (-42, "-2"),
        (-99, "-9"),
        (-100, "0"),
        (-102, "-02"),
        (-1002, "-002"),
        (-58392, "-8392"),
        (-5907, "-907"),
    ],
)
def test_remove_first(value, expected):
    assert remove_first(value) == expected


# =========================
# Invalid input tests
# =========================

@pytest.mark.parametrize(
    "value",
    [
        1.5,
        -3.14,
        "123",
        "",
        None,
        [],
        [123],
        {},
        True,
        False,
    ],
)
def test_invalid_inputs(value):
    with pytest.raises(TypeError):
        count_digits(value)

    with pytest.raises(TypeError):
        remove_last(value)

    with pytest.raises(TypeError):
        remove_first(value)


# =========================
# Large integer tests
# =========================

def test_large_integer():
    number = 10 ** 1000

    assert count_digits(number) == 1001
    assert count_digits(-number) == 1001

    assert remove_last(number) == 10 ** 999
    assert remove_last(-number) == -(10 ** 999)

    assert remove_first(number) == "0" * 1000
    assert remove_first(-number) == "0"