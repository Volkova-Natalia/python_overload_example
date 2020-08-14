"""
You can use only KEYWORD arguments for overload and (if you want) QUANTITY of positional arguments (with using keyword arguments).
For example:

___CAN:___
overloaded_function(*, kwarg1)
overloaded_function(*, kwarg2)

___CAN:___
overloaded_function(arg1, *, kwarg1)
overloaded_function(arg1, arg2, *, kwarg1)

___MUST NOT:___
overloaded_function(arg1, *, kwarg1)
overloaded_function(arg2, *, kwarg1)

___MUST NOT:___
overloaded_function(arg1)
overloaded_function(arg1, arg2)
"""

from doctest import testmod
from collections import Counter


def overload(*functions_list):
    """
    >>> overloaded_function()
    'called overloaded_function()'

    >>> overloaded_function(kwarg1=1021)
    'called overloaded_function(*, kwarg1=1021)'
    >>> overloaded_function(kwarg2=2022)
    'called overloaded_function(*, kwarg2=2022)'
    >>> overloaded_function(kwarg3=3023, kwarg4=4023)
    'called overloaded_function(*, kwarg3=3023, kwarg4=4023)'
    >>> overloaded_function(kwarg4=4024, kwarg3=3024)
    'called overloaded_function(*, kwarg3=3024, kwarg4=4024)'

    >>> overloaded_function(1031, kwarg1=1031)
    'called overloaded_function(arg1, *, kwarg1=1031)'
    >>> overloaded_function(arg1=1032, kwarg1=1032)
    'called overloaded_function(arg1, *, kwarg1=1032)'
    >>> overloaded_function(1033, kwarg2=2033)
    'called overloaded_function(arg1, *, kwarg2=2033)'
    >>> overloaded_function(arg1=1034, kwarg2=2034)
    'called overloaded_function(arg1, *, kwarg2=2034)'
    >>> overloaded_function(1035, kwarg3=3035, kwarg4=4035)
    'called overloaded_function(arg1, *, kwarg3=3035, kwarg4=4035)'
    >>> overloaded_function(1036, kwarg4=4036, kwarg3=3036)
    'called overloaded_function(arg1, *, kwarg3=3036, kwarg4=4036)'
    >>> overloaded_function(arg1=1037, kwarg3=3037, kwarg4=4037)
    'called overloaded_function(arg1, *, kwarg3=3037, kwarg4=4037)'
    >>> overloaded_function(arg1=1038, kwarg4=4038, kwarg3=3038)
    'called overloaded_function(arg1, *, kwarg3=3038, kwarg4=4038)'

    >>> overloaded_function(1041, 2041, kwarg1=1041)
    'called overloaded_function(arg1, arg2, *, kwarg1=1041)'
    >>> overloaded_function(1042, arg2=2042, kwarg1=1042)
    'called overloaded_function(arg1, arg2, *, kwarg1=1042)'
    >>> overloaded_function(arg1=1043, arg2=2043, kwarg1=1043)
    'called overloaded_function(arg1, arg2, *, kwarg1=1043)'
    >>> overloaded_function(1044, 2044, kwarg2=2044)
    'called overloaded_function(arg1, arg2, *, kwarg2=2044)'
    >>> overloaded_function(1045, arg2=2045, kwarg2=2045)
    'called overloaded_function(arg1, arg2, *, kwarg2=2045)'
    >>> overloaded_function(arg1=1046, arg2=2046, kwarg2=2046)
    'called overloaded_function(arg1, arg2, *, kwarg2=2046)'
    >>> overloaded_function(1047, 2047, kwarg3=3047, kwarg4=4047)
    'called overloaded_function(arg1, arg2, *, kwarg3=3047, kwarg4=4047)'
    >>> overloaded_function(1048, arg2=2048, kwarg3=3048, kwarg4=4048)
    'called overloaded_function(arg1, arg2, *, kwarg3=3048, kwarg4=4048)'
    >>> overloaded_function(arg1=1049, arg2=2049, kwarg3=3049, kwarg4=4049)
    'called overloaded_function(arg1, arg2, *, kwarg3=3049, kwarg4=4049)'
    """
    def function(*args, **kwargs):
        # print('kwargs.keys() =', list(kwargs.keys()))
        # print('functions_list =', functions_list)
        for current_function in functions_list:
            if len(args)+len(kwargs) != len(current_function.__code__.co_varnames):
                continue
            current_function_args = []
            current_function_kwargs = []
            if len(args) > 0:
                current_function_args = list(current_function.__code__.co_varnames)[:len(args)]
                # print('args ', args)
                # print('current_function.__code__.co_varnames ', current_function.__code__.co_varnames)
                # print('current_function_args ', current_function_args)
            if len(current_function.__code__.co_varnames) > len(args):
                current_function_kwargs = list(current_function.__code__.co_varnames)[len(args):]
            # print('current_function_kwargs ', current_function_kwargs)
            if Counter(list(kwargs.keys())) == Counter(current_function_kwargs):
                if len(current_function_args) == len(args):
                    # print('!!!!! ', list(kwargs.keys()), current_function_kwargs)
                    return current_function(*args, **kwargs)
    return lambda *args, **kwargs: function(*args, **kwargs)


overloaded_function = overload(
    lambda:   'called overloaded_function()',

    lambda *, kwarg1:           'called overloaded_function(*, kwarg1=' + str(kwarg1) + ')',
    lambda *, kwarg2:           'called overloaded_function(*, kwarg2=' + str(kwarg2) + ')',
    lambda *, kwarg3, kwarg4:   'called overloaded_function(*, kwarg3=' + str(kwarg3) + ', kwarg4=' + str(kwarg4) + ')',

    lambda arg1, *, kwarg1:           'called overloaded_function(arg1, *, kwarg1=' + str(kwarg1) + ')',
    lambda arg1, *, kwarg2:           'called overloaded_function(arg1, *, kwarg2=' + str(kwarg2) + ')',
    lambda arg1, *, kwarg3, kwarg4:   'called overloaded_function(arg1, *, kwarg3=' + str(kwarg3) + ', kwarg4=' + str(kwarg4) + ')',

    lambda arg1, arg2, *, kwarg1:           'called overloaded_function(arg1, arg2, *, kwarg1=' + str(kwarg1) + ')',
    lambda arg1, arg2, *, kwarg2:           'called overloaded_function(arg1, arg2, *, kwarg2=' + str(kwarg2) + ')',
    lambda arg1, arg2, *, kwarg3, kwarg4:   'called overloaded_function(arg1, arg2, *, kwarg3=' + str(kwarg3) + ', kwarg4=' + str(kwarg4) + ')',
)


if __name__ == '__main__':
    testmod(name='overload', verbose=True)
