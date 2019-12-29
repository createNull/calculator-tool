from datetime import timedelta
from timeit import default_timer as timer
from typing import List, Union


def fibonacci(n: int) -> int:
    """Iterative implementation of Fibonacci algorithm.
    fibonacci(0) = 0
    fibonacci(1) = 1

    :param n: positive integer
    """
    first, sec = 0, 1
    if n == 0:
        return first
    elif n == 1:
        return sec
    else:
        for i in range(2, n):
            temp = first
            first, sec = sec, temp + sec
        return sec


def ackermann(m: int, n: int) -> int:
    """Recursive implementation of Ackermann algorithm.

    :param m: positive integer
    :param n: positive integer
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def factorial(n: int) -> int:
    """Iterative implementation of factorial algorithm.
    factorial(0) = 1
    factorial(1) = 1

    :param n: positive integer
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def get_result(algorithm_name: str, params: List[int]) -> Union[str, List[int]]:
    """Gets the result calculated with the given algorithm and its execution time in seconds.

    :param algorithm_name: string with the algorithm name as value
    :param params: list of variables that should be passed as
                             parameters to the algorithm function

    :return result: list for valid input or error message for invalid input
    :return exec_time_with_decimals: float with 6 decimals

    :except RecursionError: returns string 'Please choose smaller integers.'
                            followed by error message

    """
    err_msg = "Please input only positive integers"
    elements = []

    for param in params:
        try:
            num = int(param)
            if num < 0:
                return err_msg
        except (ValueError, TypeError):
            return err_msg
        elements.append(num)

    timer_start = timer()
    try:
        result = eval(f'{algorithm_name.lower()}(*elements)')  # algorithm function call
    except RecursionError as e:
        return f'Please input smaller integers, error: {e}'
    timer_end = timer()

    exec_time = timedelta(seconds=timer_end - timer_start).total_seconds()
    exec_time_with_decimals = f'{exec_time:.6f}'
    return [result, exec_time_with_decimals]
