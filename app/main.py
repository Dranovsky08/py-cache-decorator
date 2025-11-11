from typing import Callable


def cache(func: Callable) -> Callable:
    saved_results = {}


    def wrapper(*args):
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            saved_results[args] = result
            return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
