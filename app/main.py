import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    # Write your code here
    cashe_dict = {}

    @functools.wraps(func)
    def wrapper(*args) -> dict:
        if args in cashe_dict:
            print("Getting from cache ")
            return cashe_dict[args]
        else:
            print("Calculating new result")
            cashe_dict[*args] = func(*args)
            return func(*args)
    return wrapper
