from datetime import timedelta
from timeit import default_timer as timer


def fibonacci(n):
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


def ackermann(m, n):
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


def factorial(n):
    """Iterative implementation of factorial algorithm.
    factorial(0) = 1
    factorial(1) = 1

    :param n: positive integer
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def convert_to_positive_int(user_input):
    """User input is converted from a string to an integer greater or equal to 0.

    :param user_input: string of characters given by user
    :return number: integer greater or equal to 0
    :return -1: if number is negative

    :except TypeError, ValueError
    """
    try:
        number = int(user_input)
        if number < 0:
            return -1
        return number
    except (TypeError, ValueError):
        return -1


def get_result_and_exec_time(algorithm_name, params):
    """Gets the result calculated with the given algorithm and its execution time in seconds.

    :param algorithm_name: string with the algorithm name as value
    :param params: the variables that should be passed as
                             parameters to the algorithm function
    :return result: integer if value equals an integer greater than 0
                    string "Please enter only integers, greater or equal to 0."
                    if value equals -1
    :return exec_time_with_decimals: float with 6 decimals

    :except RecursionError: returns string 'Please choose smaller integers.'
                            followed by error message

    """
    err_msg = "Please enter only integers, greater or equal to 0."
    elements = []
    exec_time_with_decimals = ''

    for param in params:
        value = convert_to_positive_int(param)
        if value == -1:
            return err_msg, exec_time_with_decimals
        elements.append(value)

    timer_start = timer()
    try:
        result = eval(f'{algorithm_name.lower()}(*elements)')  # algorithm function call
    except RecursionError as e:
        return f'Please choose smaller integers. Error: {e}', exec_time_with_decimals
    timer_end = timer()
    exec_time = timedelta(seconds=timer_end - timer_start).total_seconds()
    exec_time_with_decimals = f'{exec_time:.6f}'
    return result, exec_time_with_decimals
