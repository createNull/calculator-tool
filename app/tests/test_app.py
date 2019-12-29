from pytest import mark, raises

from app.utils import *


@mark.parametrize("test_input,expected", [(0, 0), (1, 1), (10, 34)])
def test_fibonacci(test_input, expected):
    assert fibonacci(test_input) == expected


@mark.parametrize("test_input_1,test_input_2,expected", [(0, 99, 100), (4, 0, 13), (2, 25, 53)])
def test_ackermann(test_input_1, test_input_2, expected):
    assert ackermann(test_input_1, test_input_2) == expected


def test_max_recursion_depth():
    with raises(RecursionError):
        assert ackermann(4, 2)


@mark.parametrize("test_input,expected", [(0, 1), (1, 1), (10, 3628800)])
def test_factorial(test_input, expected):
    assert factorial(test_input) == expected


@mark.parametrize("algorithm_name,test_input", [("Fibonacci", [-52]), ("Fibonacci", ['^&*']),
                                                ("Ackermann", [-55, 24]), ("Ackermann", [17, -28]),
                                                ("Ackermann", [76, '%$^']), ("Ackermann", ['abc', 85]),
                                                ("Factorial)", [-40]), ("Factorial)", ["#&*"])])
def test_invalid_input_error_message(algorithm_name, test_input):
    assert get_result(algorithm_name, test_input) == (
        "Please enter only integers, greater or equal to 0."
    )


def test_recursion_error_message():
    assert get_result("Ackermann", [5, 6]) == (
        "Please choose smaller integers. Error: maximum recursion depth exceeded in comparison"
    )
