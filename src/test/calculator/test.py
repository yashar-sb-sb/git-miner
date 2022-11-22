import re

import pytest

from src.main.calculator.calculator import add


@pytest.mark.parametrize("input_numbers, expected", [
    ("", 0),
    ("1", 1),
    ("2", 2),
    ("1,2", 3),
    ("2,2", 4),
    ("4,7,10", 21),
    ("1\n2", 3),
    ("1,2\n3", 6),
    ("//:\n7:2", 9),
    ("//:\n9:4", 13),
    ("//:\n94:5", 99),
    ("//;\n1;3", 4),
    ("//|\n1|2|3", 6),
    ("//sep\n2sep5", 7),
    ("//|\n1|2|3|1001|1", 7),
    ("//|\n1|2|3|1000|1", 1007),
])
def test_correct(input_numbers, expected):
    assert add(input_numbers) == expected


@pytest.mark.parametrize("input_numbers, error", [
    ("1,", "invalid"),
    ("//|\n1;3", "`|' expected but `;' found at position 1."),
    ("//,\n1;3", "`,' expected but `;' found at position 1."),
    ("//,\n1#3", "`,' expected but `#' found at position 1."),
    ("//#\n1#3,4", "`#' expected but `,' found at position 3."),
    ("1,-2", "Negative number(s) not allowed: -2"),
    ("2,-4,-9", "Negative number(s) not allowed: -4, -9"),
    ("//|\n1|2,-3", "Negative number(s) not allowed: -3\n`|' expected but `,' found at position 3."),
])
def test_incorrect(input_numbers, error):
    with pytest.raises(Exception, match=re.escape(error)):
        add(input_numbers)
